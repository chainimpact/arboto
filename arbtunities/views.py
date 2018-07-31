from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from exchanges.models import Ask, Bid
from datetime import datetime
from django.core import serializers
from django.conf import settings
# import sys, os
# sys.path.append(os.path.join(settings.BASE_DIR,'pyarboto/'))
from pyarboto import config

# just some testing
def index(request):			
	return HttpResponse('hey')

def monitor(request):		
	return render(request, 'arbtunities/monitor.html')	

def monitor_data(request):
	pair = request.GET.get('pair', 'ETHEUR')
	exchange = request.GET.get('exch', 'kraken')
	count = request.GET.get('count', 1000) # to-do: replace by time fraime (1h, 4h, 1d, etc)	
	o = {'pair': pair, 'exchange': exchange, 'data': get_weighted_price(exchange, pair, int(count))};
	return JsonResponse(o, safe=False)

def rois(request):		
	return render(request, 'arbtunities/rois.html')
	
def get_weighted_price(exchange='kraken', pair='ETHEUR', count=100):
	step = 50;
	# get all distinct timestamps, starting from the newest
	timestamps = Ask.objects.filter(exchange__name=exchange, pair=pair, volume__gt=0).order_by('-timestamp').values_list('timestamp').distinct()[:count:step]
	p_vs_t = []

	for t in timestamps:
		# t is a 1-tuple (--> t[0])
		asks_t = Ask.objects.filter(exchange__name=exchange, pair=pair, timestamp=t[0])
		bids_t = Bid.objects.filter(exchange__name=exchange, pair=pair, timestamp=t[0])

		if asks_t and bids_t and asks_t[0].volume and bids_t[0].volume :
			# do something
			vol = 0
			price_avg = 0
			for a, b in zip(asks_t, bids_t):
				vol = vol + a.volume + b.volume
				price_avg = price_avg + a.value*a.volume + b.value*b.volume
			price_avg = price_avg/vol
			p_vs_t.append({'timestamp': t[0], 'price_avg': price_avg})		
	# array is reversed to be ordered in time
	p_vs_t.reverse()	
	return p_vs_t

def get_hi_bids_and_lo_asks(request):
	o = []		
	fee = 0.5/100 # assuming a relatively high fee of .5%

	for mkt in config.MARKETS:
		hi_bid = 0
		hi_bid_vol = -1
		hi_bid_exch = ""
		lo_ask = 1e10
		lo_ask_vol = -1
		lo_ask_exch = ""
		for key in config.EXCHANGES:			
			client = config.EXCHANGES[key]				
			if mkt in client.get_markets():
				order_type = 'bids'
				data = client.get_n_last_orders(order_type, mkt, 1)
				if data:
					data = data[0]
					price = float(data['price'])
					vol = float(data['amount'])
					if price > hi_bid:
						hi_bid = price
						hi_bid_vol = vol
						hi_bid_exch = key;
				order_type = 'asks'
				data = client.get_n_last_orders(order_type, mkt, 1)
				if data:
					data = data[0]
					price = float(data['price'])
					vol = float(data['amount'])
					if price < lo_ask:
						lo_ask = price
						lo_ask_vol = vol
						lo_ask_exch = key;

		if hi_bid > lo_ask:
			roi = (hi_bid*(1-fee)/(lo_ask*(1+fee)) - 1)*100
		else:
			roi = 0

		o.append({'market': mkt,'hi_bid': hi_bid, 'hi_bid_vol': hi_bid_vol, 'hi_bid_exch': hi_bid_exch, 
			'lo_ask': lo_ask, 'lo_ask_vol': lo_ask_vol, 'lo_ask_exch': lo_ask_exch, 'roi': roi})
	
	return JsonResponse(o, safe=False)
	# return HttpResponse(o)


