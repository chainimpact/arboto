import os
import pytz
from django.core.management.base import BaseCommand, CommandError
from django.utils.dateparse import parse_datetime

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

class Command(BaseCommand):
    help = 'importing prices from pyarboto data files'

    def add_arguments(self, parser):
        parser.add_argument(
            "-i", "--initial",
            action="store_true",
            dest='initial',
            help='do initial import with all lines of files.')

    def handle(self, *args, **options):
        for data_file in os.listdir('/home/felipe/code/chainimpact/pyarboto/pyarboto/data'):
            if data_file.endswith('placeholder'):
                break
            with open(os.path.join('/home/felipe/code/chainimpact/pyarboto/pyarboto/data', data_file)) as f:
                try:
                    exchange = self.get_exchange(data_file)
                    price_type = self.get_price_type(data_file)
                    pair = self.get_pair(data_file)

                    data = f.readlines()
                    # import all files and all lines of files
                    if options['initial']:
                        for line in data:
                            self.import_data(line, exchange, price_type, pair)
                    # only import last line from file, this action will be done every 5 minutes,
                    # just like the cronjob for the requests.
                    else:
                        last_line = data[-1]
                        self.import_data(last_line, exchange, price_type, pair)

                    # # check if already imported
                    # if len(data) > 1:
                    #     penultimate_line = data[-2]
                    #
                    #     # if self.check_date_previous_import(penultimate_line):
                except:
                    print('ERROR!')
                    print('PASSING...')


    def get_exchange(self, data_file):
        try:
            print("data_file")
            print(data_file)
            exchanges = EXCHANGES
            for possible_exchange in exchanges:
                if data_file.lower().startswith(possible_exchange.lower()):
                    exchange = possible_exchange
            return Exchange.objects.get(name=exchange)
        except UnboundLocalError:
            print('NOT FOUND EXCHANGE')
            print('PASSING...')
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
            print(last_line)
            # print(exchange)
            # print(price_type)
            # print(pair)
            # print(date)
            # print(price)
            # print(volume)
            # for point in data_points[2::2]:
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
                t1 = Ask.objects.filter(
                    timestamp = date,
                    exchange = exchange,
                    pair = pair,
                    value = price,
                    volume = volume
                )
                t2 = Bid.objects.filter(
                    timestamp = date,
                    exchange = exchange,
                    pair = pair,
                    value = price,
                    volume = volume
                )
                print(t1)
                print(t2)
                print(new_data_point)
                new_data_point.save()
