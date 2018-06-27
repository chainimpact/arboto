""" cryptomkt exchange module.
	Supported markets:
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

def get_last_order(ordertype, market):
	"""
    :param ordertype: <str> 'buy' or 'sell'    
    :param market: <str> e.g. 'ETHEUR'
    :return: <dict> e.g. {'amount': '0.067', 'price': '400.1'}
    """			
	r = get_orderbook(ordertype, market)
	last_order = {'price': r['data'][0]['price'], 'amount': r['data'][0]['amount']}
	return last_order

def get_n_last_orders(ordertype, market, n):
	"""
    :param ordertype: <str> 'buy' or 'sell'    
    :param market: <str> e.g. 'ETHEUR'
    :return: <list> e.g. [{'amount': '0.067', 'price': '400.1'},...]
    """		
	r = get_orderbook(ordertype, market)
	last_orders = []
	# last_n_elements = 
	for elem in r['data'][0:n]:
		last_orders.append({'price': elem['price'], 'amount': elem['amount']})
	
	return last_orders

def get_orderbook(ordertype, market):
	"""
	returns bids or asks from the orderbook in json format
	"""
	payload = {'market': market, 'type': ordertype, 'page': 0}
	r = requests.get("https://api.cryptomkt.com/v1/book", params=payload) 
	if r.status_code == requests.codes.ok:
		return r.json()
	else:
		return None	

def print_markets():
	"""
	Lists all available markets.
	"""	
	r = requests.get("https://api.cryptomkt.com/v1/market")
	if r.status_code == requests.codes.ok:
		for mkt in r.json()['data']:
			print(mkt)
	else:
		print('Error')



if __name__ == '__main__':  
  
	ordertype = 'buy'
	market = 'ETHEUR'

	if get_orderbook(ordertype, market) is None:
		print("Bad response. Exiting...")
		exit()

	last_order = get_last_order(ordertype, market)
	if not isinstance(last_order, dict) or (len(last_order) != 2):
		print('Error. Function get_last_order should return a dictionary with two elements.')
		exit()

	n_last_orders = get_n_last_orders(ordertype, market, 5)
	if not isinstance(n_last_orders, list) or (len(n_last_orders) == 0):
		print('Error. Function get_n_last_orders should return a list. API not responding?')
		exit()

