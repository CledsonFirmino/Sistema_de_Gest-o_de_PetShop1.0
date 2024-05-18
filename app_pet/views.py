from django.shortcuts import render, redirect, HttpResponse
from .models import Cadastro_cliente
from .forms import CadastroClienteForm
from .models import Cadastro_pet
from .forms import CadastroPetForm
from .models import Cadastro_venda
from .forms import CadastroVendaForm
from django.contrib.auth.decorators import login_required

#---------------------------------------------------------------------------------
# LÓGICA DE CADASTRO DOS CLIENTES
#---------------------------------------------------------------------------------

def cliente (request):
    dados_cliente = {
        'dados_cliente': Cadastro_cliente.objects.all()
    }
    return render (request, 'cad_clientes/clientes.html',context=dados_cliente)

def detalhe_cliente (request ,id_cliente):
    dados_c = {
        'dados':Cadastro_cliente.objects.get(pk=id_cliente)
    }
    return render (request,'cad_clientes/detalhe_cliente.html', dados_c)

@login_required
def criar_cliente (request):
    if request.method == 'POST':
        form_cliente = CadastroClienteForm(request.POST)
        if form_cliente.is_valid():
            form_cliente.save()
            return redirect('cliente')
    else:
        cliente_form = CadastroClienteForm()
        form_cliente = {
        'form_cliente': cliente_form             
        }
        return render (request, 'cad_clientes/novo_cliente.html', context=form_cliente)

@login_required    
def editar_cliente(request,id_cliente):
    cliente = Cadastro_cliente.objects.get(pk=id_cliente)
            #novo_cadastro/1 -> GET
    if request.method == 'GET':
            form_cliente = CadastroClienteForm(instance=cliente)
            return render (request, 'cad_clientes/novo_cliente.html', {'form_cliente': form_cliente})
            #caso requisição seja POST
    else:
        form_cliente =  CadastroClienteForm(request.POST, instance=cliente)
        if form_cliente.is_valid():
               form_cliente.save()
        return redirect('cliente') 
    
@login_required    
def excluir_cliente (request,id_cliente):
    cliente = Cadastro_cliente.objects.get(pk=id_cliente)
    if request.method =='POST':
         cliente.delete()
         return redirect('cliente')
    # Aqui no item deve-se escolher e passar o que deseja referneciar do banco de dados, ex.: nome, idade etc
    # na página html, neste caso confirmar_exclusao.html
    #  <h1 style="text-align:center;">Confirmar exclusão do Cliente, {{item.nome_cliente}} ? </h1>
    return render (request, 'cad_clientes/exclusao_cliente.html', {'item': cliente}
    )

#---------------------------------------------------------------------------------
# LÓGICA DE CADASTRO DOS PETS
#---------------------------------------------------------------------------------
def pet (request):
    dados_pet = {
        'dados_pet': Cadastro_pet.objects.all()
    }
    return render (request, 'cad_pets/pets.html',context=dados_pet)

def detalhe_pet (request ,id_pet):
    dados_p = {
        'dados_p':Cadastro_pet.objects.get(pk=id_pet)
    }
    return render (request,'cad_pets/detalhe_pet.html', dados_p)

@login_required
def criar_pet (request):
    if request.method == 'POST':
        form_pet = CadastroPetForm(request.POST)
        if form_pet.is_valid():
            form_pet.save()
            return redirect('pet')
    else:
        pet_form = CadastroPetForm()
        form_pet = {
        'form_pet': pet_form             
        }
        return render (request, 'cad_pets/novo_pet.html', context=form_pet)

@login_required    
def editar_pet(request,id_pet):
    pet = Cadastro_pet.objects.get(pk=id_pet)
            #novo_cadastro/1 -> GET
    if request.method == 'GET':
            form_pet = CadastroPetForm(instance=pet)
            return render (request, 'cad_pets/novo_pet.html', {'form_pet': form_pet})
            #caso requisição seja POST
    else:
        form_pet =  CadastroPetForm(request.POST, instance=pet)
        if form_pet.is_valid():
               form_pet.save()
        return redirect('pet') 
    
@login_required    
def excluir_pet (request,id_pet):
    pet = Cadastro_pet.objects.get(pk=id_pet)
    if request.method =='POST':
         pet.delete()
         return redirect('pet')
    # Aqui no item deve-se escolher e passar o que deseja referneciar do banco de dados, ex.: nome, idade etc
    # na página html, neste caso confirmar_exclusao.html
    #  <h1 style="text-align:center;">Confirmar exclusão do Cliente, {{item.nome_cliente}} ? </h1>
    return render (request, 'cad_pets/exclusao_pet.html', {'item': pet}
    )

#---------------------------------------------------------------------------------
# LÓGICA DE CADASTRO DAS VENDAS/SERVIÇOS
#---------------------------------------------------------------------------------


def venda (request):
    dados_venda = {
        'dados_venda': Cadastro_venda.objects.all()
    }
    return render (request, 'cad_vendas/vendas.html', context=dados_venda)

def detalhe_venda (request ,id_venda):
    dados_v = {
        'dados_v':Cadastro_venda.objects.get(pk=id_venda)
    }
    return render (request,'cad_vendas/detalhe_venda.html', dados_v)

@login_required
def criar_venda (request):
    if request.method == 'POST':
        form_venda = CadastroVendaForm(request.POST)
        if form_venda.is_valid():
            form_venda.save()
            return redirect('venda')
    else:
        venda_form = CadastroVendaForm()
        form_venda = {
        'form_venda': venda_form             
        }
        return render (request, 'cad_vendas/nova_venda.html', context=form_venda)    

@login_required    
def editar_venda(request,id_venda):
    venda = Cadastro_venda.objects.get(pk=id_venda)
            #novo_cadastro/1 -> GET
    if request.method == 'GET':
            form_venda = CadastroVendaForm(instance=venda)
            return render (request, 'cad_vendas/nova_venda.html', {'form_venda': form_venda})
            #caso requisição seja POST
    else:
        form_venda =  CadastroVendaForm(request.POST, instance=venda)
        if form_venda.is_valid():
               form_venda.save()
        return redirect('venda') 
    
@login_required    
def excluir_venda (request,id_venda):
    venda = Cadastro_venda.objects.get(pk=id_venda)
    if request.method =='POST':
         venda.delete()
         return redirect('venda')
    # Aqui no item deve-se escolher e passar o que deseja referênciar do banco de dados, ex.: nome, idade etc
    # na página html, neste caso confirmar_exclusao.html
    #  <h1 style="text-align:center;">Confirmar exclusão do Cliente, {{item.nome_cliente}} ? </h1>
    return render (request, 'cad_vendas/exclusao_venda.html', {'item': venda}
    )