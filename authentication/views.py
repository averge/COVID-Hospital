from django.shortcuts import render, redirect
from proyecto_covid.helpers import login_required
from medicos.models import JefeSistema, Medico
from django.contrib import messages


def autenticar(user, password):
    return user.password == password


def login(request):
    if not request.session.get("username"):
        if request.method == 'POST':
            if request.POST.get("username"):
                try:
                    user = JefeSistema.objects.get(usuario=request.POST.get("username"))
                    tipo_medico = "jefe"
                except JefeSistema.DoesNotExist:
                    try:
                        user = Medico.objects.get(usuario=request.POST.get("username"))
                        tipo_medico = "Doctor"
                        request.session["sistema_medico"] = user.sistema.name
                    except Medico.DoesNotExist:
                        messages.error(request, 'Username or password is incorrect.')
                        return render(request, 'authentication/login.html', {})
                if not autenticar(user, request.POST.get("password")):
                    messages.error(request, 'Username or password is incorrect.')
                    return render(request, 'authentication/login.html', {})
                request.session["username"] = user.usuario
                request.session["tipo_medico"] = tipo_medico
                if tipo_medico == "jefe":
                    return redirect("sistemas.index")
                else:
                    return redirect("sistemas.show", user.sistema.name)
        return render(request, 'authentication/login.html', {})
    return redirect('sistemas.index')


@login_required
def logout(request):
    del request.session["username"]
    del request.session["tipo_medico"]
    if request.session.get("sistema_medico"):
        del request.session["sistema_medico"]
    return redirect('authentication.login')
