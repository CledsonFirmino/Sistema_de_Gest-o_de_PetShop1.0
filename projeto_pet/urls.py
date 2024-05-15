from django.contrib import admin
from django.urls import path
from app_pet import views
from app_usuarios import views as usuario_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # usuario - admin
    # senha Cfn150481$
    path('admin/', admin.site.urls),
    path('conta/', usuario_views.novo_usuario, name="novo_usuario"),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path("", views.cliente, name="clientes"),
    path("novo_cadastro/", views.criar, name="novo_cadastro"),
    path("novo_cadastro/<int:id_cliente>", views.editar, name="editar"),
    path("excluir_cliente/<int:id_cliente>", views.excluir, name="excluir"),
    path("<int:id_cliente>", views.detalhe, name="detalhe"),
]
