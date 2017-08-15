from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from rest_framework.parsers import JSONParser

from .filters import BitFilter, CoinFilter
from .models import Coin
from .serializers import CoinSerializer


@login_required
@csrf_exempt
def coin_list(request):

    if request.method == 'GET':
        # Get coins
        coins = Coin.objects.all()

        # Apply multiple filters
        filtered_coins = CoinFilter(request.GET, queryset=coins)
        bit_filter = BitFilter(request.GET, queryset=filtered_coins.qs)

        # Serialize the data
        serializer = CoinSerializer(bit_filter.qs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CoinSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@login_required
@csrf_exempt
def coin_detail(request, pk):
    try:
        coin = Coin.objects.get(pk=pk)
    except Coin.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CoinSerializer(coin)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CoinSerializer(coin, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        coin.delete()
        return HttpResponse(status=204)