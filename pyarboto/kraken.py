""" API client implementation for Kraken.
	Kraken currently supports the following markets:
		'ETCUSD',
		'ETHCAD',
		'GNOUSD',
		'DASHEUR',
		'REPBTC',
		'BCHUSD',
		'BTCJPY',
		'ETHCAD',
		'BTCUSD',
		'XRPEUR',
		'XRPJPY',
		'ICNBTC',
		'BCHEUR',
		'REPETH',
		'XLMEUR',
		'DASHXBT',
		'REPEUR',
		'LTCBTC',
		'BTCGBP',
		'LTCUSD',
		'ETHJPY',
		'BTCGBP',
		'ICNETH',
		'GNOETH',
		'EOSEUR',
		'GNOEUR',
		'GNOBTC',
		'EOSUSD',
		'EOSETH',
		'XLMBTC',
		'ETCBTC',
		'ZECBTC',
		'XRPUSD',
		'MLNETH',
		'ZECUSD',
		'DASHUSD',
		'XRPBTC',
		'LTCEUR',
		'ZECEUR',
		'BCHBTC',
		'BTCCAD',
		'ETHEUR',
		'ETHBTC',
		'REPUSD',
		'BTCCAD',
		'ETHEUR',
		'MLNBTC',
		'ETCEUR',
		'XDGBTC',
		'USDTZUSD',
		'EOSBTC',
		'ZECJPY',
		'XLMUSD',
		'ETHJPY',
		'ETHBTC',
		'BTCEUR',
		'XRPCAD',
		'BTCJPY',
		'XMRUSD',
		'XMREUR',
		'ETCETH',
		'ETHUSD',
		'BTCUSD',
		'ETHGBP',
		'ETHUSD',
		'BTCEUR',
		'XMRBTC',
		'ETHGBP'
"""
import requests, re
from exchange_client_interface import *

class Kraken(ExchangeClientInterface):

	@staticmethod
	def get_n_last_orders(ordertype, market, n):
		"""
	    :param ordertype: <str> 'bids' or 'asks'    
	    :param market: <str> e.g. 'etheur' or 'eth-eur'
	    :return: <list> e.g. [{'amount': '0.067', 'price': '400.1'},...]
	    """						
		r = Kraken.get_orderbook(market)	
		last_orders = []	
		if r is not None:		
			for key, value in r['result'].items():
				for elem in value[ordertype][0:n]:
					last_orders.append({'price': elem[0], 'amount': elem[1]})	
		return last_orders	
	
	@staticmethod
	def get_orderbook(market):
		"""
		returns the orderbook in json format. Includes both bids and asks.
		:param market: <str> e.g. 'etheur' or 'eth-eur'
		:return <dict>
		"""
		market = market.replace('-','')
		market = market.replace('BTC','XBT')			
		payload = {'pair': market}
		r = requests.get("https://api.kraken.com/0/public/Depth", params=payload)	
		if r.status_code == requests.codes.ok and not r.json()['error']:
			return r.json()
		else:
			return None	

	@staticmethod
	def get_markets():
		"""
		Returns a list of all available markets in this exchange in the format ['ETHCLP', ...]
		WARNING: It is possible that not all pairs are in the standard notation.
		"""
		markets = []
		r = requests.get("https://api.kraken.com/0/public/AssetPairs")
		if r.status_code == requests.codes.ok:
			for key, value in r.json()['result'].items():			
				key = key.replace('.d','')		# some pairs are finished with .d (dark pool)
				key = key.upper()
				if re.match('^[XZ]\w{3}[XZ]\w{3}\Z', key): # some pairs are in the form 'XETHZEUR'
					key = key[1:4] + key[5:8]
				if re.match('(^[XZ]?XBT[XZ]?\w{3}\Z)|(^[XZ]?\w{3}[XZ]?XBT\Z)', key): # kraken uses 'XBT' for 'BTC'
					key = key.replace('XBT','BTC')			
				markets.append(key)			
		return markets

if __name__ == '__main__':

	market = 'etheur'
	ordertype = 'asks'	

	if Kraken.get_orderbook(market) is None:
		print("Bad response. Exiting...")
		exit()

	if len(Kraken.get_markets()) == 0:
		print("Error. get_markets returns an empty list")
		exit()	

	n = 5
	n_last_orders = Kraken.get_n_last_orders(ordertype, market, n)
	if not isinstance(n_last_orders, list) or (len(n_last_orders) != n):
		print('Error. Function get_n_last_orders should return a list. API not responding?')
		exit()
