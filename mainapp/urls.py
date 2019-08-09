from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.main, name='index'),
    path('product/', mainapp.product, name='products'),
    path('category/<int:pk>/', mainapp.category, name='category'),
    path('contacts/', mainapp.contacts, name='contacts'),
]
