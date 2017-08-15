from django.contrib import admin

from .models import Coin


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    pass
