from datetime import datetime
import threading
import cryptomkt, buda, bitstamp
import config

FILE_CMKT_ETHEUR_BIDS = 'data/cryptomkt_etheur_bids'
# FILE_BUDA_ETH_BIDS = 'data/cryptomkt_etheur_bids'
DEBUG_MODE_ON = True

def fetch_apis(depth=5):
	timestamp = str(datetime.now())
	myTimer = threading.Timer(5.0, fetch_apis)
	# myTimer.daemon = True
	myTimer.start()	

	# cryptomkt
	cmkt_etheur_bids = cryptomkt.get_n_last_orders('buy', 'ETHEUR', depth)
	if len(cmkt_etheur_bids) == depth:
		# write to file
		record_orders(timestamp, cmkt_etheur_bids, FILE_CMKT_ETHEUR_BIDS)
		say("Writing data to file " + FILE_CMKT_ETHEUR_BIDS)
		


def record_orders(timestamp, data, file_name):	
	line = timestamp
	for order in data:
		line = line + ' ' + str(order['price']) + ' ' + str(order['amount'])
	with open(file_name, 'a') as f:
			f.write(line + '\n')

def say(msg):
	if DEBUG_MODE_ON:
		print(msg)



if __name__ == '__main__':	
	fetch_apis()
