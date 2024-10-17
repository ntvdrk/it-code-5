#from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import store

# ListView — отображение списка объектов
class MyModelListView(ListView):
    model = store
    template_name = 'store/store_list.html'
    context_object_name = 'objects'

# DetailView — отображение деталей одного объекта
class MyModelDetailView(DetailView):
    model = store
    template_name = 'store/store_detail.html'
    context_object_name = 'object'

# CreateView — создание нового объекта
class MyModelCreateView(CreateView):
    model = store
    template_name = 'store/store_form.html'
    fields = ['name', 'description']

# UpdateView — обновление существующего объекта
class MyModelUpdateView(UpdateView):
    model = store
    template_name = 'store/store_form.html'
    fields = ['name', 'description']

# DeleteView — удаление объекта с подтверждением
class MyModelDeleteView(DeleteView):
    model = store
    template_name = 'store/store_confirm_delete.html'
    success_url = reverse_lazy('store-list')
