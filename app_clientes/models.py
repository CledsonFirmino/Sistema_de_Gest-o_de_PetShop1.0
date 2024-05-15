from django.db import models

# DADOS DO CLIENTE
class Cadastro_cliente (models.Model):
    # Cliente fez compra de objetos, pet ou serviços pode ou não ter pet
    nome_cliente = models.CharField(max_length=100)
    #dono_pet = models.ForeignKey(Cadastro_pet, on_delete=models.DO_NOTHING) 
    endereco = models.CharField(max_length=150)
    contato = models.CharField (max_length=20)
