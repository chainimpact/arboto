""" Bitstamp API client implementation.
	Bitstamp currently supports the following markets:
		LTC/USD
		ETH/USD
		XRP/EUR
		BCH/USD
		BCH/EUR
		BTC/EUR
		XRP/BTC
		EUR/USD
		BCH/BTC
		LTC/EUR
		BTC/USD
		LTC/BTC
		XRP/USD
		ETH/BTC
		ETH/EUR
"""
import requests
from .exchange_client_interface import *

class Bitstamp(ExchangeClientInterface):

	@staticmethod	
	def get_n_last_orders(ordertype, market, n):
		"""
	    :param ordertype: <str> 'bids' or 'asks'    
	    :param market: <str> e.g. 'etheur' or 'eth-eur'
	    :return: <list> e.g. [{'amount': '0.067', 'price': '400.1'},...]
	    """						
		r = Bitstamp.get_orderbook(market)	
		last_orders = []	
		if r is not None:
			for elem in r[ordertype][0:n]:
				last_orders.append({'price': elem[0], 'amount': elem[1]})	
		return last_orders

	@staticmethod
	def get_orderbook(market):
		"""
		returns the orderbook in json format. Includes both bids and asks.
		:param market: <str> e.g. 'etheur' or 'eth-eur'
		"""
		market = market.replace('-','')
		url = 'https://www.bitstamp.net/api/v2/order_book/' + market
		r = requests.get(url)	
		if r.status_code == requests.codes.ok:
			return r.json()
		else:
			return None

	@staticmethod
	def get_markets():
		"""
		Returns a list of all available markets in this exchange in the format ['ETHCLP', ...]
		:return: <list>
		"""
		markets = []
		r = requests.get("https://www.bitstamp.net/api/v2/trading-pairs-info/") 	
		if r.status_code == requests.codes.ok:
			for mkt in r.json():
				markets.append(mkt['name'].replace('/','').upper())
		return markets

if __name__ == '__main__':

	market = 'etheur'
	ordertype = 'asks'

	if Bitstamp.get_orderbook(market) is None:
		print("Bad response. Exiting...")
		exit()

	if len(Bitstamp.get_markets()) == 0:
		print("Error. get_markets returns an empty list")
		exit()
	
	n = 5
	n_last_orders = Bitstamp.get_n_last_orders(ordertype, market, n)
	if not isinstance(n_last_orders, list) or (len(n_last_orders) != n):
		print('Error. Function get_n_last_orders should return a list. API not responding?')
		exit()
