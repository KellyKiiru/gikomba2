
from rest_framework import parsers
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


from bales.models import Bale
from bales.serializers import BaleSerializer

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
    """
    Retrieve, update or delete a Bale instance.
    """
    def get_object(self, pk):
        try:
            return Bale.objects.get(pk=pk)
        except Bale.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bale = self.get_object(pk)
        serializer = BaleSerializer(bale)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bale = self.get_object(pk)
        serializer = BaleSerializer(bale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bale = self.get_object(pk)
        Bale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)