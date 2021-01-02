from django.forms import ModelForm, PasswordInput
from .models import Sistema


class SistemaForm(ModelForm):
    class Meta:
        model = Sistema
        fields = ('camas_infinitas',)
