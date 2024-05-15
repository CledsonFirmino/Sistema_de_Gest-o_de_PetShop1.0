from django.shortcuts import render, redirect, HttpResponse
from .models import Cadastro_pet
from .forms import CadastroPetForm
from django.contrib.auth.decorators import login_required


# def novo_cadastro (request):
#    return render( request, 'cadastros/novo_cadastro.html')

def pet (request):
    dados_pet = {
        'dados_pet': Cadastro_pet.objects.all()
    }
    return render (request, 'cad_pets/pets.html',context=dados_pet)

def detalhe (request ,id_pet):
    dados = {
        'dados':Cadastro_pet.objects.get(pk=id_pet)
    }
    return render (request,'cad_pet/detalhe.html', dados)

@login_required
def criar (request):
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
        return render (request, 'cad_pet/novo_cadastro.html', context=form_pet)

@login_required    
def editar(request,id_pet):
    pet = Cadastro_pet.objects.get(pk=id_pet)
            #novo_cadastro/1 -> GET
    if request.method == 'GET':
            form_pet = CadastroPetForm(instance=pet)
            return render (request, 'cad_pets/novo_cadastro.html', {'form_pet': form_pet})
            #caso requisição seja POST
    else:
        form_pet =  CadastroPetForm(request.POST, instance=pet)
        if form_pet.is_valid():
               form_pet.save()
        return redirect('pets') 
    
@login_required    
def excluir (request,id_pet):
    pet = Cadastro_pet.objects.get(pk=id_pet)
    if request.method =='POST':
         pet.delete()
         return redirect('pets')
    # Aqui no item deve-se escolher e passar o que deseja referneciar do banco de dados, ex.: nome, idade etc
    # na página html, neste caso confirmar_exclusao.html
    #  <h1 style="text-align:center;">Confirmar exclusão do Cliente, {{item.nome_cliente}} ? </h1>
    return render (request, 'cad_pets/confirmar_exclusao.html', {'item': pet}
    )
