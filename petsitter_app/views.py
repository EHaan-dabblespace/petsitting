from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from petsitter_app.models import Pet
from django.urls import reverse_lazy


# Pet Views


class PetListView(ListView, LoginRequiredMixin):
    """Render a list of Pets. """

    template_name = 'pet_list.html'
    model = Pet
    context_object_name = 'pets'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Pet.objects.filter(user_id=self.request.user.id)


class PetDetailView(DetailView, LoginRequiredMixin):
    """Render a Pet's Details. """

    template_name = './pet_detail.html'
    model = Pet
    context_object_name = 'pet'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Pet.objects.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet'] = Pet.objects.get(pk=self.kwargs['pk'])
        return context
