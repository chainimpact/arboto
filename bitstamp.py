import requests

def get_last_order(ordertype, market):
	"""
    :param ordertype: <str> 'bids' or 'asks'    
    :param market: <str> e.g. 'etheur'
    :return: <dict> e.g. {'amount': '0.067', 'price': '400.1'}
    """	
	r = get_orderbook(market)		
	last_order = {'price': r[ordertype][0][0], 'amount': r[ordertype][0][1]}
	return last_order

def get_n_last_orders(ordertype, market, n):
	"""
    :param ordertype: <str> 'bids' or 'asks'    
    :param market: <str> e.g. 'etheur'
    :return: <list> e.g. [{'amount': '0.067', 'price': '400.1'},...]
    """						
	r = get_orderbook(market)	
	last_orders = []	
	for elem in r[ordertype][0:n-1]:
		last_orders.append({'price': elem[0], 'amount': elem[1]})	
	return last_orders

def get_orderbook(market):
	"""
	returns the orderbook in json format. Includes both bids and asks.
	"""
	url = 'https://www.bitstamp.net/api/v2/order_book/' + market
	r = requests.get(url)	
	if r.status_code == requests.codes.ok:
		return r.json()
	else:
		return None	

if __name__ == '__main__':

	market = 'ETHEUR'
	ordertype = 'asks'

	if get_orderbook(market) is None:
		print("Bad response. Exiting...")
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
