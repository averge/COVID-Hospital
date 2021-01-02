from django.contrib import admin
from django.forms import TextInput, Textarea 
from .models import Medico, JefeSistema
from .forms import MedicoForm, JefeForm


class MedicoAdmin(admin.ModelAdmin):
    form = MedicoForm


class JefeAdmin(admin.ModelAdmin):
    form = JefeForm


admin.site.register(Medico, MedicoAdmin)
admin.site.register(JefeSistema, JefeAdmin)
