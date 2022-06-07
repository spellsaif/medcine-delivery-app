from rest_framework import generics
from .models import  Product
from .serializers import  ProductSerializer
from rest_framework import permissions


# Create your views here.
class ListProduct(generics.ListCreateAPIView):    
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer