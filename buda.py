""" buda exchange module.
	buda currently supports the following markets:
		btc-clp
		btc-cop
		eth-clp
		eth-btc
		btc-pen
		eth-pen
		eth-cop
		bch-btc
		bch-clp
		bch-cop
		bch-pen
		btc-ars
		eth-ars
		bch-ars
		ltc-btc
		ltc-clp
		ltc-cop
		ltc-pen
		ltc-ars	
"""
import requests
import re

def get_last_order(ordertype, market):
	"""
    :param ordertype: <str> 'bids' or 'asks'    
    :param market: <str> e.g. 'ETH-CLP'
    :return: <dict> e.g. {'amount': '0.067', 'price': '400.1'}
    """			
	r = get_orderbook(market)
	last_order = {}
	if r is not None:
		last_order = {'price': r['order_book'][ordertype][0][0], 'amount': r['order_book'][ordertype][0][1]}
	return last_order

def get_n_last_orders(ordertype, market, n):
	"""
    :param ordertype: <str> 'bids' or 'asks'    
    :param market: <str> e.g. 'etheur' or 'eth-eur'
    :return: <list> e.g. [{'amount': '0.067', 'price': '400.1'},...]
    """					
	r = get_orderbook(market)
	last_orders = []
	if r is not None:
		for elem in r['order_book'][ordertype][0:n]:
			last_orders.append({'price': elem[0], 'amount': elem[1]})	
	return last_orders

def get_orderbook(market):
	"""
	returns the orderbook in json format. Includes both bids and asks.
	:param market: <str> e.g. 'etheur' or 'eth-eur'
	:return: <json> the orderbook 
	"""
	if re.match('\w{6}\Z', market):
		market = market[0:3] + '-' + market[3:]		# arrange data to match AAA-BBB format	
	url = 'https://www.buda.com/api/v2/markets/' + market + '/order_book.json'
	r = requests.get(url)
	if r.status_code == requests.codes.ok:
		return r.json()
	else:
		return None

def get_markets():
	"""
	Returns a list of all available markets in this exchange in the format ['ETHCLP', ...]
	"""
	markets = []
	url = 'https://www.buda.com/api/v2/markets.json'
	r = requests.get(url)
	if r.status_code == requests.codes.ok:
		for mkt in r.json()['markets']:
			markets.append(mkt['name'].replace('-','').upper())
	return markets

if __name__ == '__main__':  
  	
	market = 'ETHBTC'
	ordertype = 'asks'
	
	if get_orderbook(market) is None:
		print("Bad response. Exiting...")
		exit()

	if len(get_markets()) == 0:
		print("Error. get_markets returns an empty list")
		exit()		

	last_order = get_last_order(ordertype, market)
	if not isinstance(last_order, dict) or (len(last_order) != 2):
		print('Error. Function get_last_order should return a dictionary with two elements.')
		exit()

	n = 5
	n_last_orders = get_n_last_orders(ordertype, market, n)
	if not isinstance(n_last_orders, list) or (len(n_last_orders) != n):
		print('Error. Function get_n_last_orders should return a list. API not responding?')
		exit()

