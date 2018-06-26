import cryptomkt

last_order = cryptomkt.get_last_order('buy', 'ETHEUR')
if not isinstance(last_order, dict) or (len(last_order) != 2):
	print('Error. Function get_last_order should return a dictionary with two elements.')
	exit()

n_last_orders = cryptomkt.get_n_last_orders('buy', 'ETHEUR', 5)
if not isinstance(n_last_orders, list) or (len(n_last_orders) == 0):
	print('Error. Function get_n_last_orders should return a list. API not responding?')
	exit()

