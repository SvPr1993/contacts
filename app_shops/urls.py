from django.urls import path
from app_shops.views import shops_views

urlpatterns = [
    path('', shops_views, name='shops'),
]