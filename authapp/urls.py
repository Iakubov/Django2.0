from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('auth/login/', authapp.login, name='login'),
    path('auth/logout/', authapp.logout, name='logout'),
]
