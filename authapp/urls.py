from django.urls import path, re_path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
    path('update/', authapp.update, name='update'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)$', authapp.verify,
            name='verify')
]
