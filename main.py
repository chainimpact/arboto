from datetime import datetime
import threading
import cryptomkt, buda, bitstamp, kraken
from config import *

def record_orders(timestamp, data, file_name):	
	line = timestamp	
	for order in data:
		line = line + ' ' + str(order['price']) + ' ' + str(order['amount'])
	with open(file_name, 'a') as f:
			f.write(line + '\n')

def dummy_data():
	dummy_data = []	
	for i in range(DEPTH):
		dummy_data.append({'price': '0.0', 'amount': '0.0'})
	return dummy_data

def say(msg, level=0):
	if DEBUG_MODE_ON:
		print(COLORS[level] + msg + COLORS[2])

if __name__ == '__main__':	
	
	timestamp = str(datetime.now())	
	say('Starting pyArboto market data monitor at ' + timestamp)
	say('Fetching pairs: ' + str(MARKETS))
	say('From: ')
	for exch in EXCHANGES:
		say('\t' + exch)
	say('Depth: ' + str(DEPTH))

	order_types = ['bids', 'asks']

for mkt in MARKETS:
	for key in EXCHANGES:

		client = EXCHANGES[key]
		exchange_name = key.upper()
		
		if mkt in client.get_markets():

			for order_type in order_types:
			
				data = client.get_n_last_orders(order_type, mkt, DEPTH)			
				file_name = DATA_DIR + exchange_name + '_' + mkt + '_' + order_type.upper()

				if data:					
					say("Writing data to file " + file_name)
					record_orders(timestamp, data, file_name)
				else:
					say('Warning: No data received (' + exchange_name + '_' + mkt + '_' + order_type.upper() + ')', 1) 					
					say("Writing NULL data to file " + file_name)
					record_orders(timestamp, dummy_data(), file_name)






