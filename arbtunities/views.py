from django.shortcuts import render
from django.http import HttpResponse
from exchanges.models import Ask, Bid
from datetime import datetime

# Create your views here.
def index(request):
	data = get_weighted_price()
	output = ', '.join([str(p['price_avg']) for p in data])
	return HttpResponse(output)

def get_weighted_price(exchange='kraken', pair='ETHEUR', count=20):
	
	# get all distinct timestamps
	timestamps = Ask.objects.filter(exchange__name=exchange, pair=pair).order_by().values_list('timestamp').distinct()[:count]
	p_vs_t = []

	for t in timestamps:
		# t is a 1-tuple (--> t[0])
		asks_t = Ask.objects.filter(exchange__name='kraken', pair='ETHEUR', timestamp=t[0])
		bids_t = Bid.objects.filter(exchange__name='kraken', pair='ETHEUR', timestamp=t[0])

		if asks_t and bids_t:
			# do something
			vol = 0
			price_avg = 0
			for a, b in zip(asks_t, bids_t):
				vol = vol + a.volume + b.volume
				price_avg = a.value*a.volume + b.value*b.volume
			price_avg = price_avg/vol

		p_vs_t.append({'timestamp': t[0], 'price_avg': price_avg})

	return p_vs_t
