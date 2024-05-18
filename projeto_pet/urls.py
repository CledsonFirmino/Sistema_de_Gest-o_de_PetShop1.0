from django.contrib import admin
from django.urls import path
from app_pet import views
from app_usuarios import views as usuario_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # usuario - admin
    # senha Cfn150481$
    # LOGIN
    path('admin/', admin.site.urls),
    path('conta/', usuario_views.novo_usuario, name="novo_usuario"),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    
    # CLIENTES
    path("", views.cliente, name="cliente"),
    path("novo_cliente/", views.criar_cliente, name="novo_cliente"),
    path("novo_usuario/<int:id_cliente>", views.editar_cliente, name="editar_cliente"),
    path("excluir_cliente/<int:id_cliente>", views.excluir_cliente, name="excluir_cliente"),
    path("<int:id_cliente>", views.detalhe_cliente, name="detalhe_cliente"),
    
    # PETS
    path("", views.pet, name="pet"),
    path("novo_pet/",views.criar_pet, name="novo_pet"),
    path("novo_usuario/<int:id_pet>", views.editar_pet, name="editar_pet"),
    path("excluir_pet/<int:id_pet>", views.excluir_pet, name="excluir_pet"),
    path("<int:id_pet>", views.detalhe_pet, name="detalhe_pet"),
    
    # VENDAS
    path("", views.venda, name="venda"),
    path("nova_venda/", views.criar_venda, name="nova_venda"),
    path("novo_usuario/<int:id_venda>", views.editar_venda, name="editar_venda"),
    path("excluir_venda/<int:id_venda>", views.excluir_venda, name="excluir_venda"),
    path("<int:id_venda>", views.detalhe_venda, name="detalhe_venda"),
]
