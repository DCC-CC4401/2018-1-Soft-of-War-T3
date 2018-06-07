from django.conf.urls import url
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='header'),
    path('productos/', views.productos, name='productos'),
    path('productos/busqueda_avanzada',views.busqueda_avanzada, name='busqueda_avanzada'),
    path('user/', views.user, name='user'),
    path('ex/', views.ex, name='ex'),
    url(r'^productos/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
    url(r'^grilla_espacios/(?P<pk>[0-9]+)/$', views.grilla_espacios_usuario, name='grilla_espacios_usuario'),
    re_path(r'^registrate/$', views.SignUpView.as_view(), name='sign_up'),
    re_path(r'^cerrar-sesion/$', views.SignOutView.as_view(), name='sign_out'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
