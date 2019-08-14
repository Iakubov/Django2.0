from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.main, name='index'),
    path('products/', mainapp.products, name='products'),
    path('category/<int:pk>/', mainapp.category, name='category'),
    path('product/<int:pk>/', mainapp.product, name='product'),
    path('contacts/', mainapp.contacts, name='contacts'),
]
