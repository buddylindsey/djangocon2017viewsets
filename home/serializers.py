from rest_framework import serializers

from .models import Coin


class CoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coin
        fields = ('id', 'name', 'symbol', 'price_usd', 'price_btc')


