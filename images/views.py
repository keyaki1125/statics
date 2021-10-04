from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .forms import CreationForm
from .models import Image


class Home(generic.TemplateView):

    template_name = 'images/home.html'


class List(generic.ListView):

    model = Image
    context_object_name = 'images'


class Detail(generic.DetailView):

    model = Image
    context_object_name = 'image'


class Create(generic.CreateView):

    model = Image
    form_class = CreationForm

    def get_success_url(self):
        return reverse('images:detail', kwargs={'pk': self.object.pk})


class Update(generic.UpdateView):

    model = Image
    form_class = CreationForm
    template_name = 'images/image_update.html'

    # def get_initial(self):
    #     """imageには初期値を渡さないようにする"""
    #     initial = super().get_initial()
    #     initial['image'] = None
    #     return initial

    def get_success_url(self):
        return reverse('images:detail', kwargs={'pk': self.object.pk})