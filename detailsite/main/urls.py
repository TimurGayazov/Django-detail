from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('detail_page/<int:pk>', detail_page, name='detail_page'),
    path('create_detail/', create_detail, name='create_detail'),
    path('delete_detail/<int:pk>', delete_detail, name='delete_detail'),
    path('update_detail/<int:pk>', UpdateDetail.as_view(), name='update_detail'),
    path('profile/', profile, name='profile'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
