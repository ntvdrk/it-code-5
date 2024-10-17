from django.urls import path
from .views import (
    MyModelListView, MyModelDetailView, MyModelCreateView, 
    MyModelUpdateView, MyModelDeleteView
)

urlpatterns = [
    path('', MyModelListView.as_view(), name='store-list'),
    path('<int:pk>/', MyModelDetailView.as_view(), name='store-detail'),
    path('create/', MyModelCreateView.as_view(), name='store-create'),
    path('<int:pk>/update/', MyModelUpdateView.as_view(), name='store-update'),
    path('store/<int:pk>/delete/', MyModelDeleteView.as_view(), name='store-delete'),
]
