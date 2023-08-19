from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from bales.models import Bale
from bales.serializers import BaleSerializer


@csrf_exempt
def bale_list(request):
    if request.method == 'GET':
        bales = Bale.objects.all()
        serializer = BaleSerializer(bales, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BaleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    
@csrf_exempt
def bale_detail(request,pk):
    try:
        bale = Bale.objects.get(pk=pk)
    except Bale.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = BaleSerializer(Bale)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BaleSerializer(Bale, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Bale.delete()
        return HttpResponse(status=204)