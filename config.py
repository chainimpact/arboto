import os

DEBUG_MODE_ON = True

DEPTH = 5

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

COLORS = {
 	0: '\033[0m',  # end color
 	1: '\033[93m', # warning
 	2: '\033[91m'  # fail
}
