from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from django_filters import rest_framework as filters

from .filters import BitFilter, CoinFilter
from .models import Coin
from .serializers import CoinSerializer


class CoinListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CoinSerializer
    filter_backends = (filters.DjangoFilterBackend, BitFilter)
    queryset = Coin.objects.all()
    filter_class = CoinFilter


class CoinDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CoinSerializer
    queryset = Coin.objects.all()