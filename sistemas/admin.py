from django.contrib import admin
from .models import Sistema, Sala, Cama
from .forms import SistemaForm


class SistemaAdmin(admin.ModelAdmin):
    form = SistemaForm

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Sistema, SistemaAdmin)
admin.site.register(Sala)
admin.site.register(Cama)
