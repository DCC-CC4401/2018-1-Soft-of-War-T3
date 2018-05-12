from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='header'),
    path('productos/', views.productos, name='productos')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
