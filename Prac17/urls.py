from django.urls import path
from pepsi import views

urlpatterns = [
    path('', views.listaestu, name='listaestu'),
    path('estudiantes/nuevo/', views.crearestu, name='crearestu'),
    path('cursos/nuevo/', views.crearcurso, name='crearcurso'),
]
