from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from exchanges.models import Ask, Bid
from datetime import datetime
from django.core import serializers

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
