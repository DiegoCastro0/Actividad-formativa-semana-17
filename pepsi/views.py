from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Estudiante, Curso
from .forms import EstudianteForm, CursoForm

# Lista de estudiantes y cursos
def listaestu(request):
    estudiantes = Estudiante.objects.select_related('curso').all()
    cursos = Curso.objects.all()
    return render(request, 'listaestud.html', {
        'estudiantes': estudiantes,
        'cursos': cursos
    })

# Crear estudiante
def crearestu(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Estudiante registrado correctamente ")
            return redirect('listaestu')
        else:
            messages.error(request, "Error al registrar estudiante ")
    else:
        form = EstudianteForm()
    return render(request, 'crearestud.html', {'form': form})

# Crear curso
def crearcurso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Curso registrado correctamente ")
            return redirect('listaestu')
        else:
            messages.error(request, "Error al registrar curso ")
    else:
        form = CursoForm()
    return render(request, 'crearcurso.html', {'form': form})
