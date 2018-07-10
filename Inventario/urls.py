from django.conf.urls import url
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Sistema de login
    re_path(r'^registrate/$', views.SignUpView.as_view(), name='sign_up'),
    re_path(r'^cerrar-sesion/$', views.SignOutView.as_view(), name='sign_out'),
    re_path(r'^$', views.SignInView.as_view(), name='sign'),

    #USUARIO PERSONA NATURAL
    #Url para perfil usurio natural
    path('user/', views.user, name='user'),

    #Url para landing page usuario
    path('productos/', views.productos, name='productos'),
    path('productos/busqueda_avanzada',views.busqueda_avanzada, name='busqueda_avanzada'),
    url(r'^grilla_espacios/(?P<pk>[0-9]+)/$', views.grilla_espacios_usuario, name='grilla_espacios_usuario'),

    #Ficha articulo persona natural
    url(r'^productos/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
    path('reservar/', views.reservarArticulo, name='reservarArticulo'),

    #USUARIO PERSONA ADMINISTRADOR
    #Urls para perfil usuario administrador
    path('user/admin/users/', views.admin_users, name='admin_users'),
    path('user/admin/inventario/', views.admin_inventario, name='admin_inventario'),
    url(r'^user/admin/grilla/(?P<pk>[0-9]+)/$', views.admin_grilla, name='admin_grilla'),

    #Ficha articulos vista administrador
    url(r'^user/admin/productos/(?P<pk>[0-9]+)/$', views.admin_producto, name='admin_article_detail'),

    path('grilla_espacios/', views.grilla_espacios_usuario, name='grilla_espacios_usuario'),
    path('user/admin/grilla/0/<int:estado_id>/', views.admin_filtrar_prestamos, name='admin_filtrar_prestamos'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
