from django.http import response
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import Categoryserializer, Productserializer
from . models import Product , Category

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/product-list',
        'Detail View' : '/product-detail/<int:id>',
        'Create' : '/product-create',
        'Update' : '/product-update/<int:id>',
        'Delete' : '/product-delete/<int:id>',

    }
    return response(api_urls)

@api_view(['GET'])
def ShowAllC(request):
    category = Category.objects.all()
    serializer1 = Categoryserializer(category, many=True)
    return Response(serializer1.data)




@api_view(['GET'])
def ShowAll(request):
    products = Product.objects.all()
    serializer = Productserializer(products, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def updateProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = Productserializer(instance=product,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
