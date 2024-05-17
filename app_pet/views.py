from django.shortcuts import render, redirect, HttpResponse
from .models import Cadastro_pet
from .forms import CadastroPetForm
from .models import Cadastro_cliente
from .forms import CadastroClienteForm
from django.contrib.auth.decorators import login_required


# LÓGICA DE CADASTRO DOS CLIENTES

def cliente (request):
    dados_cliente = {
        'dados_cliente': Cadastro_cliente.objects.all()
    }
    return render (request, 'cad_clientes/clientes.html',context=dados_cliente)

def detalhe_cliente (request ,id_cliente):
    dados = {
        'dados':Cadastro_cliente.objects.get(pk=id_cliente)
    }
    return render (request,'cad_clientes/detalhe_cliente.html', dados)

@login_required
def criar_cliente (request):
    if request.method == 'POST':
        form_cliente = CadastroClienteForm(request.POST)
        if form_cliente.is_valid():
            form_cliente.save()
            return redirect('clientes')
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
        return redirect('clientes') 
    
@login_required    
def excluir_cliente (request,id_cliente):
    cliente = Cadastro_cliente.objects.get(pk=id_cliente)
    if request.method =='POST':
         cliente.delete()
         return redirect('clientes')
    # Aqui no item deve-se escolher e passar o que deseja referneciar do banco de dados, ex.: nome, idade etc
    # na página html, neste caso confirmar_exclusao.html
    #  <h1 style="text-align:center;">Confirmar exclusão do Cliente, {{item.nome_cliente}} ? </h1>
    return render (request, 'cad_clientes/exclusao_cliente.html', {'item': cliente}
    )

# # LÓGICA DE CADASTRO DOS PETS
#-----------------------------------------------------------------------------------------
def pet (request):
    dados_pet = {
        'dados_pet': Cadastro_pet.objects.all()
    }
    return render (request, 'cad_pets/pets.html',context=dados_pet)

def detalhe_pet (request ,id_pet):
    dados = {
        'dados':Cadastro_pet.objects.get(pk=id_pet)
    }
    return render (request,'cad_pets/detalhe_pet.html', dados)

@login_required
def criar_pet (request):
    if request.method == 'POST':
        form_pet = CadastroPetForm(request.POST)
        if form_pet.is_valid():
            form_pet.save()
            return redirect('pets')
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
        return redirect('pets') 
    
@login_required    
def excluir_pet (request,id_pet):
    pet = Cadastro_pet.objects.get(pk=id_pet)
    if request.method =='POST':
         pet.delete()
         return redirect('pets')
    # Aqui no item deve-se escolher e passar o que deseja referneciar do banco de dados, ex.: nome, idade etc
    # na página html, neste caso confirmar_exclusao.html
    #  <h1 style="text-align:center;">Confirmar exclusão do Cliente, {{item.nome_cliente}} ? </h1>
    return render (request, 'cad_pets/exclusao_pet.html', {'item': pet}
    )
# # LÓGICA DE CADASTRO DAS VENDAS SERVIÇOS
#-----------------------------------------------------------------------------------------