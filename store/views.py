#from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy

from store import filters
from .models import store

from django_filters.views import FilterView

from store.models import store

#class StoreListTemplateView(TemplateView):
#    template_name = 'store/store_list.html'
#    
#    def get_context_data(self, **kwargs):
#        context =  super().get_context_data(**kwargs)
#        context['store'] = store.objects.all()
#        return context
        
# ListView — отображение списка объектов
class MyModelListView(ListView):
    model = store
    template_name = 'store/store_list.html'
    context_object_name = 'objects'
    filterset_class = filters.store

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
    success_url = reverse_lazy('store-list')

# UpdateView — обновление существующего объекта
class MyModelUpdateView(UpdateView):
    model = store
    template_name = 'store/store_form.html'
    fields = ['name', 'description']
    
    def get_success_url(self):
        return reverse_lazy("store-detail", kwargs={'pk': self.object.pk})

# DeleteView — удаление объекта с подтверждением
class MyModelDeleteView(DeleteView):
    model = store
    template_name = 'store/store_confirm_delete.html'
    success_url = reverse_lazy('store-list')
