from django.contrib import admin


from .models import Ask, Bid, Exchange


admin.site.register(Ask)
admin.site.register(Bid)

admin.site.register(Exchange)
