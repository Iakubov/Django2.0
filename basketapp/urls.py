from django.urls import path, re_path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='index'),
    path('add/<int:pk>/', basketapp.basket_add, name='add'),
    path('delete/<int:pk>/', basketapp.basket_delete, name='delete'),

    re_path('update/(?P<pk>\d+)/(?P<quantity>\d+)/', basketapp.basket_update, name='update'),
]
