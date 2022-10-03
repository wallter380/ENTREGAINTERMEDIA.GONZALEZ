import datetime
import django
import django.db.utils
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from AppCoder.forms import *
from AppCoder.models import *

from django.contrib import messages

def curso_no_editar(request):

    return render(request, 'AppCoder/curso_no_editar.html')

def estudiante_no_editar(request):

    return render(request, 'estudiante_no_editar.html')

def profesor_no_editar(request):

    return render(request, 'profesor_no_editar.html')
def editar_curso(request, camada):

    curso_editar = Curso.objects.get(camada=camada)

    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            curso_editar.nombre = data.get('nombre')

            curso_editar.camada = data.get('camada')

            try:

                curso_editar.save()

            except django.db.utils.IntegrityError:

                return redirect('AppCoderCursoNoEditar')

    contexto = {

        'form': CursoFormulario(
            initial={

                'nombre': curso_editar.nombre,
                'camada': curso_editar.camada
            }
        )
    }

    return render(request, 'Appcoder/curso_formulario.html', contexto)

def editar_estudiante(request, nombre, apellido, email):

    estudiante_editar = Estudiantes.objects.get(nombre=nombre, apellido=apellido, email=email)

    if request.method == 'POST':
        mi_formulario = EstudianteFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            estudiante_editar.nombre = data.get('nombre')

            estudiante_editar.apellido = data.get('apellido')

            estudiante_editar.email = data.get('email')

            try:

                estudiante_editar.save()

            except django.db.utils.IntegrityError:

                return redirect('AppCoderEstudianteFormulario')

    contexto = {

        'form': EstudianteFormulario(
            initial={

                'nombre': estudiante_editar.nombre,
                'apellido': estudiante_editar.apellido,
                'email': estudiante_editar.email
            }
        )
    }

    return render(request, 'Appcoder/estudiante_formulario.html', contexto)

def editar_profesor(request, nombre, apellido, email):

    profesor_editar = Profesor.objects.get(nombre=nombre, apellido=apellido, email=email)

    if request.method == 'POST':
        mi_formulario = ProfesorFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            profesor_editar.nombre = data.get('nombre')

            profesor_editar.apellido = data.get('apellido')

            profesor_editar.email = data.get('email')

            try:

                profesor_editar.save()

            except django.db.utils.IntegrityError:

                messages.error(request, "La modificacion fallo porque se repite dato.")

            return redirect('AppCoderProfesorFormulario')

    contexto = {

        'form': ProfesorFormulario(
            initial={

                'nombre': profesor_editar.nombre,
                'apellido': profesor_editar.apellido,
                'email': profesor_editar.email
            }
        )
    }

    return render(request, 'Appcoder/profesor_formulario.html', contexto)
def eliminar_profesor(request,nombre, apellido, email):

    profesor_eliminar = Profesor.objects.get(nombre=nombre, apellido=apellido, email=email )

    profesor_eliminar.delete()

    messages.info(request, f'El {profesor_eliminar} fue eliminado.')

    return render(request, 'Appcoder/profesor_eliminado.html')
def eliminar_estudiante(request, nombre, apellido, email):

    estudiante_eliminar = Estudiantes.objects.get(nombre=nombre, apellido=apellido, email=email)

    estudiante_eliminar.delete()

    messages.info(request, f'El {estudiante_eliminar} fue eliminado.')

    return render(request, 'Appcoder/estudiante_eliminado.html')
def eliminar_curso(request, camada):

    curso_eliminar = Curso.objects.get(camada=camada )

    curso_eliminar.delete()

    messages.info(request, f'El {curso_eliminar} fue eliminado.')

    return render(request, 'Appcoder/curso_eliminado.html')

def busqueda_camada_post(request):

    camada = request.GET.get('camada')

    cursos = Curso.objects.filter(camada__exact=camada)

    contexto = {

        'cursos' : cursos

    }

    return render(request, 'Appcoder/curso_filtrado.html', contexto)

@login_required
def busqueda_camada(request):

    contexto = {
        'form': BusquedaCamadaFormulario()
    }

    return render(request, 'AppCoder/busqueda_camada.html', contexto)

def curso_formulario(request):

    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            curso1 = Curso(nombre=data.get('nombre'), camada=data.get('camada'))

            try:

                curso1.save()

            except django.db.utils.IntegrityError:

                return redirect('AppCoderCursoFormulario')

    cursos = Curso.objects.all()

    contexto = {
        'form': CursoFormulario(),
        'cursos': cursos
    }

    return render(request, 'Appcoder/curso_formulario.html', contexto)

def curso_eliminado(request):

    return render(request, 'curso_eliminado.html')

def estudiante_eliminado(request):

    return render(request, 'estudiante_eliminado.html')

def profesor_eliminado(request):

    return render(request, 'profesor_eliminado.html')

def inicio(request):

    return render(request, 'index.html')

def estudiante_formulario(request):

    if request.method == 'POST':
        mi_formulario = EstudianteFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            estudiante1 = Estudiantes(nombre=data.get('nombre'), apellido=data.get('apellido'), email=data.get('email'))

            try:

                estudiante1.save()

            except django.db.utils.IntegrityError:

                return redirect('AppCoderEstudianteFormulario')

    estudiantes = Estudiantes.objects.all()

    contexto = {
        'form': EstudianteFormulario(),
        'estudiantes': estudiantes
    }

    return render(request, 'Appcoder/estudiante_formulario.html', contexto)

def busqueda_estudiante_post(request):

    nombre = request.GET.get('nombre')

    email = request.GET.get('email')

    estudiantes = Estudiantes.objects.filter(nombre__exact=nombre, email__exact=email)

    contexto = {

        'estudiantes': estudiantes

    }

    return render(request, 'Appcoder/estudiante_filtrado.html', contexto)

@login_required
def busqueda_estudiante(request):

    contexto = {
        'form': BusquedaEstudianteFormulario()
    }

    return render(request, 'AppCoder/busqueda_estudiante.html', contexto)


def profesor_formulario(request):

    if request.method == 'POST':
        mi_formulario = ProfesorFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            profesor1 = Profesor(nombre=data.get('nombre'), apellido=data.get('apellido'), email=data.get('email'))

            try:

                profesor1.save()

            except django.db.utils.IntegrityError:

                return redirect('AppCoderProfesorFormulario')


    profesores = Profesor.objects.all()

    contexto = {
        'form': EstudianteFormulario(),
        'profesores': profesores
    }

    return render(request, 'Appcoder/profesor_formulario.html', contexto)

def busqueda_profesor_post(request):

    email = request.GET.get('email')

    profesores = Profesor.objects.filter(email__exact=email)

    contexto = {

        'profesores': profesores

    }

    return render(request, 'Appcoder/profesor_filtrado.html', contexto)

@login_required
def busqueda_profesor(request):

    contexto = {
        'form': BusquedaProfesorFormulario()
    }

    return render(request, 'AppCoder/busqueda_profesor.html', contexto)



