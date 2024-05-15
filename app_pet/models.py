from django.db import models
from django.utils import timezone
from datetime import date
from models import Cadastro_cliente


OPCOES_RACA = ((1,'Border Collie'),(2,'Buldogue francês'),(3,'Buldogue inglês'),(4,'Chihuahua'),(5,'Dachshund'),
               (6,'Fila Brasileiro'),(7,'Fox Terrier'),(8,'Golden Retriever'),(9,'Husky'),(10,'Labrador'),(11,'Lhasa Apso'),
               (12,'Maltês'),(13,'Pinscher'),(14,'Poodle'),(15,'Pug'),(16,'Pastor'),(17,'Rottweiler'),(18,'Schnauzer'),(19,'Terrier'),
               (20,'Yorkshire'),(21,'Shih Tzu'),(22,'Schnauzer'),(23,'SRD (Sem Raça Definida)'))  
    
OPCOES_PORTE = ((1,'Pequeno 6 a 15kg'),(2,'Médio 15 a 25kg'),(3,'Grande 25 a 45kg'),(4,',Gigantes 45 a 90kg'))    

OPCOES_PELAGEM = ((1,'Longa'),(2,'Curta'), (3,'Encaracolado'),(4,'Dupla'),(5,'Peculiar'),(6,'Longo Ondulado'),(7,'Textura dura'),(8,'Textura lisa'),)  

OPCOES_BANHO = ((1,'Simples'),(2,'Composto'), (3,'Hidratação'),)  

OPCOES_TOSA = ((1,'Tosa Higiênica'),(2,'Tosa na Tesoura'), (3,'Tosa Verão'),(4,'Tosa na Máquina'),(5,'Tosa Bebê'),(6,'Tosa da Raça'),)               


# DADOS DO PET
class Cadastro_pet (models.Model):
    nome_pet = models.CharField(max_length=50)
    nome_dono = models.ForeignKey(Cadastro_cliente, on_delete=models.DO_NOTHING)
    idade_pet = models.IntegerField()
    data_aniversario = models.DateField()
    raca = models.CharField(max_length=50, choices=OPCOES_RACA,default='23')   
    porte = models.CharField(max_length=50, choices=OPCOES_PORTE,default='1')    
    pelagem = models.CharField(max_length=50, choices=OPCOES_PELAGEM,default='1')
      # EXEMPLO
    # def upload_path_handler(instance, filename):
    # return "uploads/%s/%s" % (instance.subpasta, filename)
#class Arquivo(models.Model):
 #   arquivo = models.FileField(upload_to=upload_path_handler)
  
    foto = models.FileField()
# DADOS DE SERVIÇO
# Obs.: Deve constar o nome do Cliente 
# e seu pet ou vários pets

class Cadastro_venda (models.Model):
    # Cliente faz compra de objetos, pets ou serviço
    # Nome do Cliente e nome do Pet a qual foi solicitado o serviço
    cliente_compra = models.ForeignKey(Cadastro_cliente, on_delete=models.DO_NOTHING)
    pet_cliente = models.ForeignKey(Cadastro_pet, on_delete=models.DO_NOTHING) 
    banho_tipo = models.CharField(max_length=50, choices=OPCOES_BANHO)
    valor_banho = models.FloatField()
    tosa_tipo = models.CharField(max_length=50, choices=OPCOES_TOSA,default='1')
    valor_tosa = models.FloatField()
    item = models.CharField(max_length=100)
    valor_item = models.FloatField()
    data = models.DateTimeField(auto_now_add=True)
    # django.utils.timezone.now
    data_agendada = models.DateField()
    observacao = models.TextField(max_length=255)
 

   
# class MyModel(models.Model):
 #   date = models.DateField(default=date.today) # Here
 #   datetime = models.DateTimeField(default=timezone.now) # Here
