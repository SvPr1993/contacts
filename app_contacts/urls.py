from django.urls import path, include
from app_contacts.views import contacts_views, contacts_detail_views

urlpatterns = [
    path('', contacts_views, name='contacts'),
    path('<int:id>/', contacts_detail_views, name='person'),
]