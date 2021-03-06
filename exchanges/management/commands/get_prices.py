import os
import pytz
from django.core.management.base import BaseCommand, CommandError
from django.utils.dateparse import parse_datetime
from django.db.utils import IntegrityError

import arboto
from arboto.settings import DEBUG
from exchanges.models import Ask, Bid, ApiRequest, Exchange


PRICE_TYPES = (
    ('a', 'ask'),
    ('b', 'bid')
    )

EXCHANGES = [
	'kraken',
	'bitstamp',
	'buda',
	'cryptomkt'
    ]

PAIRS = (
	('ETHEUR', 'ETHER-EURO'),
	('ETHBTC', 'ETHER-BITCOIN'),
	('ETHCLP', 'ETHER-PESOS'),
	('BTCCLP', 'BITCOIN-PESOS'),
	('LTCBTC', 'LITECOIN-BITCOIN'),
	('BCHBTC', 'BITCOINCASH-BITCOIN')
)


# paths
# OJO: we do dirname twice to go up twice to parent dir
BASE_DIR = os.path.dirname(os.path.dirname(arboto.settings.__file__))
DATA_DIR = os.path.join(BASE_DIR,'pyarboto/data/')

class Command(BaseCommand):
    help = 'importing prices from pyarboto data files'

    def add_arguments(self, parser):
        parser.add_argument(
            "-i", "--initial",
            action="store_true",
            dest='initial',
            help='do initial import with all lines of files.')

        parser.add_argument(
            '-n', '--number-of-lines',
            required=False,
            dest='number_of_lines',
            help="set 'n' number of lines to read from the bottom of the files")

    def handle(self, *args, **options):
        for data_file in os.listdir(DATA_DIR):
            if data_file.endswith('placeholder'):
                break
            with open(os.path.join(DATA_DIR, data_file)) as f:
                exchange = self.get_exchange(data_file)
                price_type = self.get_price_type(data_file)
                pair = self.get_pair(data_file)

                data = f.readlines()
                # import all files and all lines of files
                if options['initial']:
                    # looping through all lines in data, might take a while
                    for line in data:
                        self.import_data(line, exchange, price_type, pair)

                # getting the number_of_lines var from the options and importing that
                elif options.get('number_of_lines'):
                    number_of_lines = int(options.get('number_of_lines'))
                    n_lines = data[-number_of_lines:]
                    for line in n_lines:
                        self.import_data(line, exchange, price_type, pair)
                # only import last line from file, this action will be done every 5 minutes,
                # just like the cronjob for the requests.
                else:
                    last_line = data[-1]
                    self.import_data(last_line, exchange, price_type, pair)
                # TODO:
                # # check if already imported

    def get_exchange(self, data_file):
        try:
            exchanges = EXCHANGES
            for possible_exchange in exchanges:
                if data_file.lower().startswith(possible_exchange.lower()):
                    exchange = possible_exchange
            return Exchange.objects.get(name=exchange)
        except UnboundLocalError:
            print('NOT FOUND EXCHANGE')
            print('PASSING...')
            # TODO recover new exchange
            pass

    def get_price_type(self, data_file):
        if data_file.endswith('ASKS'):
            return 'a'
        return 'b'

    def get_pair(self, data_file):
        return data_file[-11:-5]

    def check_if_already_imported(self, last_line):
        date_sting = last_line[:16]
        parse_datetime(date_sting)
        if Ask.objects.filter(timestamp=date) or \
           Bid.objects.filter(timestamp=date):
            return True
        else:
            # TODO: re-import data from previous date
            pass

    def check_date_previous_import(self, penultimate_line):
        date_sting = penultimate_line[:16]
        parse_datetime(date_sting)
        if Ask.objects.filter(timestamp=date):
            # check if
            return True
        else:
            # TODO: re-import data from previous date
            pass

    def add_timezone(self, date_obj):
        date = pytz.timezone("Europe/Paris").localize(date_obj)
        return date

    def import_data(self, last_line, exchange, price_type, pair):
        date_sting = last_line[:16]
        date = parse_datetime(date_sting)
        date = self.add_timezone(date)

        data_points = last_line.split()

        for price, volume in zip(data_points[2::2], data_points[3::2]):
            try:
                if price_type == 'a':
                    new_data_point = Ask(
                        timestamp = date,
                        exchange = exchange,
                        pair = pair,
                        value = price,
                        volume = volume
                    )
                    new_data_point.save()
                else:
                    new_data_point = Bid(
                        timestamp = date,
                        exchange = exchange,
                        pair = pair,
                        value = price,
                        volume = volume
                    )
                    new_data_point.save()

            except IntegrityError:
                print('IntergrityError, passing import.')
                print('PASSING...')
