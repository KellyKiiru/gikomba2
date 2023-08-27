from rest_framework import viewsets
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


from bales.models import *
from bales.serializers import *

class BaleList(APIView):
    """
    List all bales or create a new bale.
    """
    def get(self, request, format=None):
        bales = Bale.objects.all()
        serializer = BaleSerializer(bales, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BaleDetail(APIView):

    def get(self,pk, request, format=None):
        bale = Bale.objects.get(pk)
        serializer = BaleSerializer(bale)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,pk, request, format=None):
        bale = Bale.objects.get(pk)
        serializer = BaleSerializer(bale)

    def delete(self,pk, request, format=None):
        bale = Bale.objects.get(pk)
        bale.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)













# class BaleViewSet(viewsets.ModelViewSet): 
#     queryset = Bale.objects.all()
#     serializer_class = BaleSerializer


# class StoreViewSet(viewsets.ModelViewSet):
#     queryset = Store.objects.all()
#     serializer_class = StoreSerializer