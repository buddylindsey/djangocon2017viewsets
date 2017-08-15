import django_filters

from rest_framework import filters

from .models import Coin


class CoinFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Coin
        fields = ('name', 'symbol',)


# Only show results with `bit` in the name
class BitFilter(filters.BaseFilterBackend):

    class Meta:
        model = Coin
        fields = ('name',)

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(name__icontains='bit')