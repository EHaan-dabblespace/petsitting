from django.urls import path
from .views import PetListView

urlpatterns = [
    path('pets/', PetListView.as_view(), name='pet_list')
]
