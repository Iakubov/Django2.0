from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp


urlpatterns = [
    path('admin/', admin.site.urls,),

    path('', include('mainapp.urls', namespace='main')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('myadmin/', include('adminapp.urls', namespace='myadmin')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)