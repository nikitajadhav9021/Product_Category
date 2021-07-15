from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview,name='apiOverview'),
    path('category-list/',views.ShowAllC,name='category-list'),
    path('product-list/',views.ShowAll,name='product-list'),
    path('update/<int:pk>/',views.updateProduct,name='update')

]
