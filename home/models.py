from django.db import models


class Coin(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    price_usd = models.DecimalField(
        max_digits=20, decimal_places=2, null=True)
    price_btc = models.DecimalField(
        max_digits=50, decimal_places=20, null=True)
