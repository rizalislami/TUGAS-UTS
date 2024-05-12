from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import penjualan
from .serializers import PenjualanSerializer

@csrf_exempt
def penjualan_detail(request, pk, format=None):
    try:
        penjualans = penjualan.objects.get(pk=pk)
    except penjualan.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PenjualanSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PenjualanSerializer(penjualans, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        penjualans.delete()
        return HttpResponse(status=204)