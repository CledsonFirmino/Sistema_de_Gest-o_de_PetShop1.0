from django.forms import ModelForm
from .models import Cadastro_pet
from .models import Cadastro_cliente
from .models import Cadastro_venda


class CadastroClienteForm(ModelForm):

    class Meta:
        model = Cadastro_cliente
        fields = "__all__"


class CadastroPetForm(ModelForm):

    class Meta:
        model = Cadastro_pet
        fields = "__all__"


class CadastroVendaForm(ModelForm):

    class Meta:
        model = Cadastro_venda
        fields = "__all__"
