from django.contrib import admin
from .models import Cadastro_cliente
from .models import Cadastro_pet
from .models import Cadastro_venda


admin.site.register(Cadastro_cliente)
admin.site.register(Cadastro_pet)
admin.site.register(Cadastro_venda)

                    
