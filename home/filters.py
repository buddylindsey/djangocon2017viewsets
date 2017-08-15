import django_filters

from .models import Coin

class CoinFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Coin
        fields = {
            'symbol': ['exact'],
            'name': ['iexact'],
        }


# Only show results with `bit` in the name
class BitFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method='filter_name')

    class Meta:
        model = Coin
        fields = ('name',)

    def filter_name(self, queryset, name, value):
        return queryset.filter(name__icontains='bit')