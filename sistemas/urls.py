from django.urls import path

from . import views

urlpatterns = [
    path('<str:name>/show/', views.show, name='sistemas.show'),
    path('', views.index, name='sistemas.index'),
]