from django.db import models



PRICE_TYPES = (
    ('a', 'ask'),
    ('b', 'bid')
    )

PAIRS = (
	('ETHEUR', 'ETHER-EURO'),
	('ETHBTC', 'ETHER-BITCOIN'),
	('ETHCLP', 'ETHER-PESOS'),
	('BTCCLP', 'BITCOIN-PESOS'),
	('LTCBTC', 'LITECOIN-BITCOIN'),
	('BCHBTC', 'BITCOINCASH-BITCOIN')
)

class Exchange(models.Model):
    """
    the actual exchange model. an instance can be easily added through shell command or admin.
    """
    name = models.CharField(max_length=200)
    website = models.URLField(max_length=1000)
    api_url = models.URLField(max_length=1000)
    # api_version = models.CharField(max_length=5)

    def __str__(self):
        return "{}".format(self.name)

    def get_new_exchages():
        pass


class ApiRequest(models.Model):
    """
    This data is recorded for legacy purposes. It has the old way of storing data, with each request
    having a timestamp, and 10 data points for each Ask and Bid.
    """
    timestamp = models.DateTimeField('datetime requested')
    # values would be stored in char format representing a python list, which would then need to be
    # converted to an actual list
    values = models.CharField(max_length=150)



class Price(models.Model):
    """
    abstract model of a bid or ask.
    """
    timestamp = models.DateTimeField('datetime requested')
    value = models.DecimalField(max_digits=16, decimal_places=10)
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    # api_request FK is also a legacy artifact to be deleted later on
    api_request = models.ForeignKey(ApiRequest, on_delete=models.CASCADE, blank=True, null=True)
    pair = models.CharField(choices=PAIRS, default='ETHEUR', max_length=6)
    volume = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        abstract = True


class Ask(Price):
    price_type = models.CharField(choices=PRICE_TYPES, default='a', max_length=1)

    def __str__(self):
        return "{}-{}-{}-{}-{}-{}".format(
            self.exchange,
            self.timestamp,
            self.price_type.upper(),
            self.pair,
            self.value,
            self.volume
            )


class Bid(Price):
    price_type = models.CharField(choices=PRICE_TYPES, default='b', max_length=1)

    def __str__(self):
        return "{}-{}-{}-{}-{}-{}".format(
            self.timestamp,
            self.exchange,
            self.price_type.upper(),
            self.pair,
            self.value,
            self.volume
            )
