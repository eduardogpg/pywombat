
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
