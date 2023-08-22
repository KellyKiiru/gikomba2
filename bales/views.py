
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
    

class StoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer