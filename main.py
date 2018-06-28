from datetime import datetime
import threading
import cryptomkt, buda, bitstamp
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
	say('Starting pyArboto at ' + timestamp)
	say('Fetching markets: ' + str(MARKETS))
	say('Depth: ' + str(DEPTH))

	for mkt in MARKETS:

		# 1. fetch data from cryptomkt
		if mkt in cryptomkt.get_markets():
			# get crytomkt bids
			data = cryptomkt.get_n_last_orders('buy', mkt, DEPTH)
			file_name = DATA_DIR + 'CRYPTOMKT_' + mkt + '_BIDS'
			if len(data) != 0:				
				say("Writing data to file " + file_name)
				record_orders(timestamp, data, file_name)
			else:
				say('Warning: No data received (CRYPTOMKT_' + mkt + '_BIDS)', 1)
				say("Writing NULL data to file " + file_name)
				record_orders(timestamp, dummy_data(), file_name)
 
			# get crytomkt asks
			data = cryptomkt.get_n_last_orders('sell', mkt, DEPTH)
			file_name = DATA_DIR + 'CRYPTOMKT_' + mkt + '_ASKS'
			if len(data) != 0:
				say("Writing data to file " + file_name)		
				record_orders(timestamp, data, file_name)
			else:
				say('Warning: No data received (CRYPTOMKT_' + mkt + '_ASKS', 1)
				say("Writing NULL data to file " + file_name)
				record_orders(timestamp, dummy_data(), file_name)

		# 2. fetch data from buda
		if mkt in buda.get_markets():
			# get buda bids
			data = buda.get_n_last_orders('bids', mkt, DEPTH)
			file_name = DATA_DIR + 'BUDA_' + mkt + '_BIDS'
			if len(data) != 0:
				say("Writing data to file " + file_name)		
				record_orders(timestamp, data, file_name)
			else:
				say('Warning: No data received (BUDA_' + mkt + '_BIDS)', 1)
				say("Writing NULL data to file " + file_name)
				record_orders(timestamp, dummy_data(), file_name)

			# get buda asks
			data = buda.get_n_last_orders('asks', mkt, DEPTH)
			file_name = DATA_DIR + 'BUDA_' + mkt + '_ASKS'
			if len(data) != 0:
				say("Writing data to file " + file_name)		
				record_orders(timestamp, data, file_name)
			else:
				say('Warning: No data received (BUDA_' + mkt + '_ASKS)', 1)
				say("Writing NULL data to file " + file_name)
				record_orders(timestamp, dummy_data(), file_name)

		# 3. fetch data from bitstamp
		if mkt in bitstamp.get_markets():
			# get bitstamp bids
			data = bitstamp.get_n_last_orders('bids', mkt, DEPTH)
			file_name = DATA_DIR + 'BITSTAMP_' + mkt + '_BIDS'
			if len(data) != 0:
				say("Writing data to file " + file_name)		
				record_orders(timestamp, data, file_name)
			else:
				say('Warning: No data received (BITSTAMP_' + mkt + '_BIDS)', 1)
				say("Writing NULL data to file " + file_name)
				record_orders(timestamp, dummy_data(), file_name)

			# get bitstamp asks
			data = bitstamp.get_n_last_orders('asks', mkt, DEPTH)
			file_name = DATA_DIR + 'BITSTAMP_' + mkt + '_ASKS'
			if len(data) != 0:
				say("Writing data to file " + file_name)		
				record_orders(timestamp, data, file_name)
			else:
				say('Warning: No data received (BITSTAMP_' + mkt + '_ASKS)', 1)
				say("Writing NULL data to file " + file_name)
				record_orders(timestamp, dummy_data(), file_name)



