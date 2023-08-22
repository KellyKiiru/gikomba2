
from rest_framework import viewsets
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


from bales.models import *
from bales.serializers import *

class BaleViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = Bale.objects.all()
    serializer_class = BaleSerializer

class StoreList(APIView):
    """Returns the list of stores"""
    def get(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(request):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreDetail(APIView):
    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        store = self.get_object(pk)
        store.delete()
        return Response(ststus=status.HTTP_204_NO_CONTENT)