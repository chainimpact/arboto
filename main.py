from datetime import datetime
import threading
import cryptomkt, buda

CMKT_BIDS_FILE = 'data/cryptomkt_bids'

def fetch_apis():
	myTimer = threading.Timer(5.0, fetch_apis)
	# myTimer.daemon = True
	myTimer.start()
	with open(CMKT_BIDS_FILE, 'a') as f:
		read_data = f.write(str(cryptomkt.get_last_order('buy', 'ETHEUR')) + '\n')
	print('cryptomkt bid (ETHEUR): ' + str(cryptomkt.get_last_order('buy', 'ETHEUR')))
	# print('buda bid (ETHEUR): ' + str(buda.get_last_order('asks', 'ETH-CLP')))

if __name__ == '__main__':
	fetch_apis()
