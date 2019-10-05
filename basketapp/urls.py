from django.urls import path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='index'),
    path('add/<int:pk>/', basketapp.basket_add, name='add'),
    path('delete/<int:pk>/', basketapp.basket_delete, name='delete'),

    path('update/<int:pk>/<int:quantity>/', basketapp.basket_update, name='update'),
]
