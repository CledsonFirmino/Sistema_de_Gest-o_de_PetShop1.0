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
    # CLIENTES
    path("", views.cliente, name="cliente"),
    path("novo_cliente/", views.criar_cliente, name="novo_cliente"),
    path("novo_cliente/<int:id_cliente>", views.editar_cliente, name="editar_cliente"),
    path("exclusao_cliente/<int:id_cliente>", views.excluir_cliente, name="excluir_cliente"),
    path("<int:id_cliente>", views.detalhe_cliente, name="detalhe_cliente"),
    # PETS
    path("", views.pet, name="pet"),
    # VENDAS
   # path("", views.vendas, name="vendas"),
]
