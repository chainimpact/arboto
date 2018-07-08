from django.db import models

PRICE_TYPES = (
    ('a', 'ask'),
    ('b', 'bid')
    )

class Exchange(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(max_length=1000)
    api_url = models.URLField(max_length=1000)
    # api_version = models.CharField(max_length=5)

    def __str__(self):
        return "{}".format(self.name)


class Price(models.Model):
    timestamp = models.DateTimeField('date published')
    value = models.DecimalField(max_digits=16, decimal_places=10)
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Ask(Price):
    price_type = models.CharField(choices=PRICE_TYPES, default='a', max_length=1)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.exchange, self.timestamp, self.price_type, self.value)


class Bid(Price):
    price_type = models.CharField(choices=PRICE_TYPES, default='a', max_length=1)

    def __str__(self):
        return "{}-{}-{}".format(self.exchange, self.timestamp, self.value)
