from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from petsitter_app.models import Pet
from django.urls import reverse_lazy


# Pet Views


class PetListView(LoginRequiredMixin, ListView):
    template_name = 'pet_list.html'
    model = Pet
    context_object_name = 'pets'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Pet.objects.filter(user_id=self.request.user.id)
