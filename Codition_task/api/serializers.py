from rest_framework import fields, serializers
from .models import Product , Category


class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' 

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 