from django.db import models
from django.utils import timezone
from datetime import date


# DADOS DO CLIENTE
class Cadastro_cliente (models.Model):
    # Cliente fez compra de objetos, pet ou serviços pode ou não ter pet
    nome_cliente = models.CharField(max_length=50)
    #dono_pet = models.ForeignKey(Cadastro_pet, on_delete=models.DO_NOTHING) 
    endereco = models.CharField(max_length=150)
    contato = models.CharField (max_length=20)
# DADOS DO PET
class Cadastro_pet (models.Model):
    nome_pet = models.CharField(max_length=50)
    nome_dono = models.ForeignKey(Cadastro_cliente, on_delete=models.DO_NOTHING)
    idade_pet = models.IntegerField()
    data_aniversario = models.DateField()
    raca = models.CharField(max_length=50)
    porte = models.CharField(max_length=50)
    pelagem = models.CharField(max_length=50)
    foto = models.FileField()
# DADOS DE SERVIÇO
# Obs.: Deve constar o nome do Cliente 
# e seu pet ou vários pets

class Cadastro_venda (models.Model):
    # Cliente faz compra de objetos, pets ou serviço
    # Nome do Cliente e nome do Pet a qual foi solicitado o serviço
    cliente_compra = models.ForeignKey(Cadastro_cliente, on_delete=models.DO_NOTHING)
    pet_cliente = models.ForeignKey(Cadastro_pet, on_delete=models.DO_NOTHING) 
    banho_tipo = models.CharField(max_length=255)
    valor_banho = models.FloatField()
    tosa_tipo = models.CharField(max_length=255)
    valor_tosa = models.FloatField()
    item = models.CharField(max_length=100)
    valor_item = models.FloatField()
    data = models.DateTimeField(default=timezone.now())
    data_agendada = models.DateField()
    observacao = models.TextField(max_length=255)
 

   
# class MyModel(models.Model):
 #   date = models.DateField(default=date.today) # Here
 #   datetime = models.DateTimeField(default=timezone.now) # Here
