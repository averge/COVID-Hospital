from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('authentication/', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('pacientes/', include('pacientes.urls')),
    path('', include('sistemas.urls')),
    path('systems/', include('medicos.urls')),
    path('alerts/', include('reglas.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
