from django.forms import ModelForm
from .models import Cadastro_pet

class CadastroPetForm(ModelForm):

        class Meta:
            model = Cadastro_pet
            fields = '__all__'