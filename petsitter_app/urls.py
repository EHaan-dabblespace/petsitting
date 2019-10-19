from django.urls import path
from .views import *

urlpatterns = [
    path('pets/', PetListView.as_view(), name='pet_list'),
    path('pets/create', PetCreateView.as_view(), name='pet_create'),
    path('pets/<int:pk>', PetDetailView.as_view(), name='pet_detail'),
    path('pets/<int:pk>/update', PetUpdateView.as_view(), name='pet_update'),
    path('pets/<int:pk>/delete', PetDeleteView.as_view(), name='pet_delete'),

    path('families/', FamilyListView.as_view(), name='family_list'),
    path('families/create', FamilyCreateView.as_view(), name='family_create'),
    path('families/<int:pk>', FamilyDetailView.as_view(), name='family_detail'),
    path('families/<int:pk>/update',
         FamilyUpdateView.as_view(), name='family_update'),
    path('families/<int:pk>/delete',
         FamilyDeleteView.as_view(), name='family_delete'),
]
