from rest_framework import serializers
from .models import loginaccount, registeraccount, product

class productSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = product
        fields = ('name', 'price')

class loginserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = loginaccount
        fields = ('username', 'password')

class registerserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = registeraccount
        fields = ('username', 'password')
    