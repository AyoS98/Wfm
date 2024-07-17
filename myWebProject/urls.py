
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('myWebApp.urls')),
    path('', include('myWebApp.urls')),
    # path('artisanform', include('myWebApp.urls')),
    # path('cr7', include('myWebApp.urls')),
    # path('messi', include('myWebApp.urls')),
    # path('login', include('myWebApp.urls')),
    # path('register', include('myWebApp.urls')),
    # path('logout', include('myWebApp.urls')),
    path('success', include('myWebApp.urls')),
   


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
