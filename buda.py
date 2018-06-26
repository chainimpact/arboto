import requests

def get_last_order(ordertype, market):
	"""
    :param ordertype: <str> 'bids' or 'asks'    
    :param market: <str> e.g. 'ETH-CLP'
    :return: <dict> e.g. {'amount': '0.067', 'price': '400.1'}
    """		
	url = 'https://www.buda.com/api/v2/markets/' + market + '/order_book.json'
	r = requests.get(url)
	r = r.json()			
	last_order = {'price': r['order_book'][ordertype][0][0], 'amount': r['order_book'][ordertype][0][1]}
	return last_order

def get_n_last_orders(ordertype, market, n):
	"""
    :param ordertype: <str> 'bids' or 'asks'    
    :param market: <str> e.g. 'ETH-CLP'
    :return: <list> e.g. [{'amount': '0.067', 'price': '400.1'},...]
    """				
	url = 'https://www.buda.com/api/v2/markets/' + market + '/order_book.json'
	r = requests.get(url).json()	
	last_orders = []
	for elem in r['order_book'][ordertype][0:n]:
		last_orders.append({'price': elem[0], 'amount': elem[1]})	
	return last_orders

if __name__ == '__main__':  
  
	# just a test...
	# print(get_last_order('bids', 'ETH-CLP'))
	print(get_n_last_orders('bids', 'ETH-CLP', 5))