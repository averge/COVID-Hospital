from django.urls import path

from . import views

urlpatterns = [
    path('<str:name>/doctors/', views.index, name='medicos.index'),
    path('<str:name>/doctors/change_system/<int:id_m>', views.change_system, name='medicos.change_system'),
]
