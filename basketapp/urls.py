from django.urls import path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('auth/login/', basketapp.index, name='index'),
]
