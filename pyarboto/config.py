import os
from . import kraken, bitstamp, buda, cryptomkt

DEBUG_MODE_ON = True

# colors for printing debug messages
COLORS = {
 	0: '\033[0m',  # end color
 	1: '\033[93m', # warning
 	2: '\033[91m'  # fail
}

# number of orders to fetch from the orderbook
DEPTH = 20

MARKETS = (
	'ETHEUR',
	'ETHBTC',
	'ETHCLP',
	'BTCCLP',
	'LTCBTC',
	'BCHBTC'
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR,'data/')

# these are the exchanges that will be fetched
EXCHANGES = {
	'kraken': kraken.Kraken,
	'bitstamp': bitstamp.Bitstamp,
	'buda': buda.Buda,
	'cryptomkt': cryptomkt.Cryptomkt,
}
