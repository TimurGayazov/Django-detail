from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('detail_page/<int:pk>', detail_page, name='detail_page'),
    path('create_detail/', create_detail, name='create_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
