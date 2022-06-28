from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from .serializers import productSerializer, registerserializer,loginserializer
from .models import product,registeraccount,loginaccount
from myapu import serializers

class productviewset(viewsets.ModelViewSet):
    queryset = product.objects.all().order_by('name')
    serializers_class = productSerializer
class loginviewset(viewsets.ModelViewSet):
    queryset = loginaccount.objects.all().order_by('username')
    serializers_class = loginaccount
class registerviewset(viewsets.ModelViewSet):
    queryset = registeraccount.objects.all().order_by('username')
    serializers_class = registerserializer


