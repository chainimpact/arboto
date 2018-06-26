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
	payload = {'market': market, 'type': ordertype, 'page': 0}
	return requests.get("https://api.cryptomkt.com/v1/book", params=payload).json()


if __name__ == '__main__':  
  
  # just a test...
  # print(get_last_order('buy', 'ETHEUR'))
  print(get_n_last_orders('buy', 'ETHEUR', 5))