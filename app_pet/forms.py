from django.forms import ModelForm
from .models import Cadastro_pet
from .models import Cadastro_cliente

class CadastroClienteForm(ModelForm):
    
        class Meta:
            model = Cadastro_cliente
            fields = '__all__'

class CadastroPetForm(ModelForm):

        class Meta:
            model = Cadastro_pet
            fields = '__all__'

           

