from django import forms
from .models import Evolucion

mv_choices = (
    ("good", 'Good'),
    ("regular", 'Regular'),
    ("bad", 'Bad'),
)

tipo_choices = (
    ("normal", "Normal"),
    ("pathologic", "Pathologic"),
)


class EvolucionForm(forms.ModelForm):
    temperatura = forms.DecimalField(label="Temperature")
    ta_sistolica = forms.IntegerField(label="Systolic pressure")
    ta_diastolica = forms.IntegerField(label="Diastolic pressure")
    frecuencia_cardiaca = forms.IntegerField(label="Heart rate")
    frecuencia_respiratoria = forms.IntegerField(label="Respiratory rate")
    mecanica_ventilatoria = forms.ChoiceField(
        label="Respiratory mechanics",
        choices=mv_choices,
        widget=forms.RadioSelect,
    )
    requiere_o2_suplementario = forms.BooleanField(
        label="Requires suplementary O2",
        required=False,
    )
    canula_nasal = forms.IntegerField(
        label="Nasal cannula",
        min_value=1,
        max_value=6,
        required=False,
    )
    mascara_con_reservorio = forms.DecimalField(
        label="Non-rebreather mask",
        min_value=1,
        max_value=100,
        required=False,
    )
    saturacion_o2 = forms.IntegerField(label="O2 saturation", required=False)
    pafi = forms.BooleanField(label="PaFi", required=False)
    pafi_valor = forms.IntegerField(label="PaFi value", required=False)
    prono_vigil = forms.BooleanField(label="Prone position", required=False)
    tos = forms.BooleanField(label="Cough", required=False)
    disnea = forms.IntegerField(
        label="Shortness of breath",
        min_value=0,
        max_value=4,
        required=False,
    )
    estabilidad_respiratoria = forms.BooleanField(label="Respiratory estability", required=False)
    somnolencia = forms.BooleanField(label="Somnolence", required=False)
    anosmia = forms.BooleanField(label="Anosmia", required=False)
    disgeusia = forms.BooleanField(label="Dysgeusia", required=False)
    rx_tx = forms.BooleanField(label="Chest radiography", required=False)
    tipo_rx_tx = forms.ChoiceField(
        label="Chest radiography type",
        widget=forms.RadioSelect,
        choices=tipo_choices,
        required=False,
    )
    descripcion_patologico_rx_tx = forms.CharField(
        label="Chest radiography description",
        widget=forms.Textarea(
            attrs={
                'rows': 3,
                'cols': 50
            }
        ),
        required=False,
    )
    tac_torax = forms.BooleanField(label="Chest tomography", required=False)
    tipo_tac_torax = forms.ChoiceField(
        label="Chest tomography type",
        widget=forms.RadioSelect,
        choices=tipo_choices,
        required=False,
    )
    descripcion_patologico_tac_torax = forms.CharField(
        label="Chest tomography description",
        widget=forms.Textarea(
            attrs={
                'rows': 3,
                'cols': 50
            }
        ),
        required=False,
    )
    ecg = forms.BooleanField(label="Electrocardiography", required=False)
    tipo_ecg = forms.ChoiceField(
        label="Electrocardiography type",
        widget=forms.RadioSelect,
        choices=tipo_choices,
        required=False,
    )
    descripcion_patologico_ecg = forms.CharField(
        label="Electrocardiography description",
        widget=forms.Textarea(
            attrs={
                'rows': 3,
                'cols': 50
            }
        ),
        required=False,
    )
    pcr_covid = forms.BooleanField(label="PCR", required=False)
    tipo_pcr_covid = forms.ChoiceField(
        label="PCR type",
        widget=forms.RadioSelect,
        choices=tipo_choices,
        required=False,
    )
    descripcion_pcr_covid = forms.CharField(
        label="PCR description",
        widget=forms.Textarea(
            attrs={
                'rows': 3,
                'cols': 50
            }
        ),
        required=False,
    )
    observacion = forms.CharField(
        label="Remarks",
        widget=forms.Textarea(
            attrs={
                'rows': 3,
                'cols': 50
            }
        ),
        required=False,
    )
    arm = forms.BooleanField(label="ARM", required=False)
    descripcion_arm = forms.CharField(
        label="ARM description",
        widget=forms.Textarea(
            attrs={
                'rows': 3,
                'cols': 50
            }
        ),
        required=False,
    )
    traqueostomia = forms.BooleanField(label="Tracheostomy", required=False)
    vasopresores = forms.BooleanField(label="Vasopressors", required=False)
    descripcion_vasopresores = forms.CharField(
        label="Vasopressors description",
        widget=forms.Textarea(
            attrs={
                'rows': 3,
                'cols': 50
            }
        ),
        required=False,
    )

    class Meta:
        exclude = ('fecha_carga', 'hora_carga', 'internacion')
        model = Evolucion
