from django.test import SimpleTestCase

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import mixins
from django_filters import rest_framework as filters

from .views import CoinViewSet

from .filters import BitFilter, CoinFilter
from .serializers import CoinSerializer


class CoinViewSetTest(SimpleTestCase):
    def setUp(self):
        self.view = CoinViewSet()

    def test_attrs(self):
        self.assertIsInstance(self.view, mixins.CreateModelMixin)
        self.assertIsInstance(self.view, mixins.ListModelMixin)
        self.assertIsInstance(self.view, mixins.UpdateModelMixin)
        self.assertIsInstance(self.view, mixins.RetrieveModelMixin)
        self.assertIsInstance(self.view, mixins.DestroyModelMixin)
        self.assertIsInstance(self.view, viewsets.GenericViewSet)

        self.assertEqual(self.view.permission_classes, (IsAuthenticated,))
        self.assertEqual(self.view.serializer_class, CoinSerializer)
        self.assertSequenceEqual(
            self.view.filter_backends,
            (filters.DjangoFilterBackend, BitFilter))

        self.assertEqual(self.view.filter_class, CoinFilter)