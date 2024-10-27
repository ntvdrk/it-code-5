from django.conf import settings
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from store import views

from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('store',views.StoreAPI, basename= 'store' )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name = 'schema')),
    path('', views.MyModelListView.as_view(), name='store-list'),
    path('store/<int:pk>/', views.MyModelDetailView.as_view(), name='store-detail'),
    path('create/', views.MyModelCreateView.as_view(), name='store-create'),
    path('store/<int:pk>/update/', views.MyModelUpdateView.as_view(), name='store-update'),
    path('store/<int:pk>/delete/', views.MyModelDeleteView.as_view(), name='store-delete'),
] + router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
