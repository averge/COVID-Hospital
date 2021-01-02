from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='alertas.index'),
    path('<int:id_a>/', views.marcar_vista, name='alertas.marcar_vista'),
]
