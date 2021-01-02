from django.forms import ModelForm, PasswordInput
from .models import Medico, JefeSistema


class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        widgets = {
            'password': PasswordInput(),
        }
        fields = '__all__'


class JefeForm(ModelForm):
    class Meta:
        model = JefeSistema
        widgets = {
            'password': PasswordInput(),
        }
        fields = '__all__'
