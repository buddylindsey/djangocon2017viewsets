from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import mixins

from django_filters import rest_framework as filters

from .filters import BitFilter, CoinFilter
from .models import Coin
from .serializers import CoinSerializer


class CoinViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CoinSerializer
    filter_backends = (filters.DjangoFilterBackend, BitFilter)
    queryset = Coin.objects.all()
    filter_class = CoinFilter