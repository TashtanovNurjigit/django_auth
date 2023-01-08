from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
<<<<<<< HEAD
    path('', include('cloth.urls')),
=======
>>>>>>> c7d84810f65a4ac6834e637d1c19ca9fe23c53e4
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
