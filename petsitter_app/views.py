from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pet, Family
from .forms import PetForm, FamilyForm
from django.urls import reverse_lazy

# TODO: Namespace the templates to 'family' and 'pet'

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


class PetCreateView(CreateView, LoginRequiredMixin):
    template_name = './pet_create.html'
    model = Pet
    form_class = PetForm
    success_url = reverse_lazy('pet_list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # TODO: redirect to newly created pet detail page


class PetUpdateView(UpdateView, LoginRequiredMixin):
    template_name = './pet_create.html'
    model = Pet
    form_class = PetForm
    success_url = reverse_lazy('pet_list')
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Pet.objects.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet'] = Pet.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # TODO: redirect to the updated pet's detail page


class PetDeleteView(DeleteView, LoginRequiredMixin):

    template_name = './pet_delete.html'
    model = Pet
    context_object_name = 'pet'
    success_url = reverse_lazy('pet_list')


# Family Views

class FamilyListView(ListView, LoginRequiredMixin):
    template_name = './family_list.html'
    model = Family
    context_object_name = 'families'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Family.objects.filter(user_id=self.request.user.id)


class FamilyDetailView(DetailView, LoginRequiredMixin):
    template_name = './family_detail.html'
    model = Family
    context_object_name = 'family'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Family.objects.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['family'] = Family.objects.get(pk=self.kwargs['pk'])
        return context


class FamilyCreateView(CreateView, LoginRequiredMixin):
    template_name = './family_create.html'
    model = Family
    form_class = FamilyForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('family_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # TODO: redirect to newly created family detail page


class FamilyUpdateView(UpdateView, LoginRequiredMixin):
    template_name = './family_create.html'
    model = Family
    form_class = FamilyForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('family_list')

    def get_queryset(self):
        return Family.objects.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['family'] = Family.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # TODO: redirect to the updated pet's detail page


class FamilyDeleteView(DeleteView, LoginRequiredMixin):

    template_name = './family_delete.html'
    model = Family
    context_object_name = 'family'
    success_url = reverse_lazy('family_list')
