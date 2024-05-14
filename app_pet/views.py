from django.shortcuts import render, redirect, HttpResponse
from .models import Cadastro_cliente
from .forms import CadastroClienteForm
from django.contrib.auth.decorators import login_required


# def novo_cadastro (request):
#    return render( request, 'cadastros/novo_cadastro.html')

def cliente (request):
    dados_cliente = {
        'dados_cliente': Cadastro_cliente.objects.all()
    }
    return render (request, 'cadastros/clientes.html',context=dados_cliente)

def detalhe (request ,id_cliente):
    dados = {
        'dados':Cadastro_cliente.objects.get(pk=id_cliente)
    }
    return render (request,'cadastros/detalhe.html', dados)

@login_required
def criar (request):
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
        return render (request, 'cadastros/novo_cadastro.html', context=form_cliente)

@login_required    
def editar(request,id_cliente):
    cliente = Cadastro_cliente.objects.get(pk=id_cliente)
            #novo_cadastro/1 -> GET
    if request.method == 'GET':
            form_cliente = CadastroClienteForm(instance=cliente)
            return render (request, 'cadastros/novo_cadastro.html', {'form_cliente': form_cliente})
            #caso requisição seja POST
    else:
        form_cliente =  CadastroClienteForm(request.POST, instance=cliente)
        if form_cliente.is_valid():
               form_cliente.save()
        return redirect('clientes') 
    
@login_required    
def excluir (request,id_cliente):
    cliente = Cadastro_cliente.objects.get(pk=id_cliente)
    if request.method =='POST':
         cliente.delete()
         return redirect('clientes')
    # Aqui no item deve-se escolher e passar o que deseja referneciar do banco de dados, ex.: nome, idade etc
    # na página html, neste caso confirmar_exclusao.html
    #  <h1 style="text-align:center;">Confirmar exclusão do Cliente, {{item.nome_cliente}} ? </h1>
    return render (request, 'cadastros/confirmar_exclusao.html', {'item': cliente}
    )
