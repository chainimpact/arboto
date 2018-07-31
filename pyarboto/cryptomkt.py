""" Cryptomkt API client implementation.
	Cryptomkt currently supports the following markets:
		ETHCLP
		ETHARS
		ETHEUR
		ETHBRL
		XLMCLP
		XLMARS
		XLMEUR
		XLMBRL
		BTCCLP
		BTCARS
		BTCEUR
		BTCBRL
"""
import requests
from .exchange_client_interface import *

class Cryptomkt(ExchangeClientInterface):

	order_dict = {'bids': 'buy', 'asks': 'sell'}

	@staticmethod
	def get_n_last_orders(ordertype, market, n):
		"""
	    :param ordertype: <str> 'bids' or 'asks'
	    :param market: <str> e.g. 'etheur' or 'eth-eur'
	    :return: <list> e.g. [{'amount': '0.067', 'price': '400.1'},...]
	    """		
		r = Cryptomkt.get_orderbook(ordertype, market)
		last_orders = []
		if r is not None: 
			for elem in r['data'][0:n]:
				last_orders.append({'price': elem['price'], 'amount': elem['amount']})	
		return last_orders

	@staticmethod
	def get_orderbook(ordertype, market):
		"""
		returns bids or asks from the orderbook in json format
		:param ordertype: <str> 'buy' or 'sell'
		:param market: <str> e.g. 'etheur' or 'eth-eur'
		"""
		market = market.replace('-','')
		order = Cryptomkt.order_dict[ordertype]
		payload = {'market': market, 'type': order, 'page': 0}
		r = requests.get("https://api.cryptomkt.com/v1/book", params=payload) 
		if r.status_code == requests.codes.ok:
			return r.json()
		else:
			return None	

	@staticmethod
	def get_markets():
		"""
		returns a list of all available markets in this exchange in the format ['ETHCLP', ...]
		:return: <list>
		"""	
		markets = []
		r = requests.get("https://api.cryptomkt.com/v1/market")	
		if r.status_code == requests.codes.ok:
			for mkt in r.json()['data']:
				markets.append(mkt.upper())
		return markets			

if __name__ == '__main__':  

	# run some simple unitary tests

	ordertype = 'bids'
	market = 'ETHEUR'

	if Cryptomkt.get_orderbook(ordertype, market) is None:
		print("Bad response. Exiting...")
		exit()

	if len(Cryptomkt.get_markets()) == 0:
		print("Error. get_markets returns an empty list")
		exit()

	n_last_orders = Cryptomkt.get_n_last_orders(ordertype, market, 5)
	if not isinstance(n_last_orders, list) or (len(n_last_orders) == 0):
		print('Error. Function get_n_last_orders should return a list. API not responding?')
		exit()

