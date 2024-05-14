from django.forms import ModelForm
from .models import Cadastro_cliente

class CadastroClienteForm(ModelForm):

        class Meta:
            model = Cadastro_cliente
            fields = '__all__'