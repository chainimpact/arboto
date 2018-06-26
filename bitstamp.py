import requests

def get_last_order(ordertype, market):
	"""
    :param ordertype: <str> 'bids' or 'asks'    
    :param market: <str> e.g. 'etheur'
    :return: <dict> e.g. {'amount': '0.067', 'price': '400.1'}
    """	
	url = 'https://www.bitstamp.net/api/v2/order_book/' + market 
	r = requests.get(url)
	r = r.json()			
	last_order = {'price': r[ordertype][0][0], 'amount': r[ordertype][0][1]}
	return last_order

def get_n_last_orders(ordertype, market, n):
	"""
    :param ordertype: <str> 'bids' or 'asks'    
    :param market: <str> e.g. 'etheur'
    :return: <list> e.g. [{'amount': '0.067', 'price': '400.1'},...]
    """					
	url = 'https://www.bitstamp.net/api/v2/order_book/' + market
	r = requests.get(url)
	r = r.json()	
	last_orders = []	
	for elem in r[ordertype][0:n-1]:
		last_orders.append({'price': elem[0], 'amount': elem[1]})
	
	return last_orders

if __name__ == '__main__':  
  
	# just a test...
	# print(get_last_order('asks', 'ETHEUR'))
	print(get_n_last_orders('asks', 'ETHEUR', 5))