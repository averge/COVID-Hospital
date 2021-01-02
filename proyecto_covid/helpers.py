from django.shortcuts import redirect
from functools import wraps
from medicos.models import Medico


def login_required(f):
    @wraps(f)
    def decorated_function(request, *args, **kwargs):
        if not request.session.get("username"):
            return redirect("authentication.login")
        return f(request, *args, **kwargs)
    return decorated_function


def permiso_required(f):
    @wraps(f)
    def decorated_function(request, *args, **kwargs):
        if request.session.get("tipo_medico") != "jefe":
            usuario = request.session.get("username")
            medico = Medico.objects.get(usuario=usuario)
            return redirect("sistemas.show", medico.sistema.name)
        return f(request, *args, **kwargs)
    return decorated_function
