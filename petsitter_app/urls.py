from django.urls import path
from .views import *

urlpatterns = [
    path('pets/', PetListView.as_view(), name='pet_list'),
    path('pets/<int:pk>', PetDetailView.as_view(), name='pet_detail'),
]
