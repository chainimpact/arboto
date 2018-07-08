from django.contrib import admin


from .models import Ask, Bid, Exchange, ApiRequest


class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'api_url')


class AskAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'exchange' ,'value')


class BidAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'exchange' ,'value')


admin.site.register(Exchange, ExchangeAdmin)

admin.site.register(ApiRequest)
admin.site.register(Ask, AskAdmin)
admin.site.register(Bid, BidAdmin)
