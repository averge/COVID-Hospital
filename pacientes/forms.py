from django import forms
from .validations import validate_email
from .models import Paciente, Internacion


class PacienteForm(forms.ModelForm):
    dni = forms.IntegerField(
        max_value=99999999,
        min_value=1000000,
        label="DNI del paciente",
        widget=forms.NumberInput(attrs={'placeholder': 'Enter patient\'s DNI'})
    )
    nombre_y_apellido = forms.CharField(label="Name and last name", strip=True)
    telefono = forms.IntegerField(label="Phone number")
    mail = forms.EmailField(label="Email", validators=[validate_email])
    obra_social = forms.CharField(label="Healthcare", required=False, strip=True)
    domicilio = forms.CharField(label="Residence", strip=True)
    antecedentes_personales = forms.CharField(
        label="Personal history",
        widget=forms.Textarea(
            attrs={
                'rows': 1,
                'cols': 200
            }
        ),
        strip=True
    )
    fecha_nacimiento = forms.DateField(
        label="Date of birth",
        widget=forms.SelectDateWidget(years=range(1900, 2021))
    )
    nombre_contacto = forms.CharField(label="First name", strip=True)
    apellido_contacto = forms.CharField(label="Last name", strip=True)
    telefono_contacto = forms.IntegerField(label="Phone number")
    parentesco_contacto = forms.CharField(label="Kinship", strip=True)

    class Meta:
        exclude = ('medicos', 'alta', 'obito')
        model = Paciente


class InternacionForm(forms.ModelForm):
    fecha_inicio_sintomas = forms.DateField(
        label="Symptoms start date",
        widget=forms.SelectDateWidget(years=range(1900, 2021))
    )
    fecha_diagnostico = forms.DateField(
        label="Diagnosis start date",
        widget=forms.SelectDateWidget(years=range(1900, 2021))
    )
    enfermedad_actual = forms.CharField(label="Current illness")
    descripcion = forms.CharField(label="Description")

    class Meta:
        exclude = ('fecha_internacion', 'fecha_egreso', "fecha_obito", "paciente")
        model = Internacion
