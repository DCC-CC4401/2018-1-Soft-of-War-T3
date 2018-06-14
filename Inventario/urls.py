from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='header'),
    path('productos/', views.productos, name='productos'),
    path('user/', views.user, name='user'),
    url(r'^productos/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
    path('grilla_espacios/', views.grilla_espacios_usuario, name='grilla_espacios_usuario'),
    #path('user/#/', views.info_reserv, name='info_reserv'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
