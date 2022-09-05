import datetime
from django.shortcuts import render, redirect
from AppCoder.forms import CursoFormulario, BusquedaCamadaFormulario, EstudianteFormulario, \
    BusquedaEstudianteFormulario, BusquedaProfesorFormulario, ProfesorFormulario
from AppCoder.models import *

def busqueda_camada_post(request):

    camada = request.GET.get('camada')

    cursos = Curso.objects.filter(camada__exact=camada)

    contexto = {

        'cursos' : cursos

    }

    return render(request, 'Appcoder/curso_filtrado.html', contexto)

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
            curso1.save()

            return redirect('AppCoderCursoFormulario')

    cursos = Curso.objects.all()

    contexto = {
        'form': CursoFormulario(),
        'cursos': cursos
    }

    return render(request, 'Appcoder/curso_formulario.html', contexto)


def inicio(request):
    return render(request, 'index.html')


#def curso(request):
#    curso1 = Curso(nombre="Python", camada=31095)
#
#    curso1.save()
#
#    contexto = {
#
#        'curso': curso1
#    }

#    return render(request, 'AppCoder/curso.html', contexto)


#def entregable(request):
#    entregables = [
#
#        {
#            'nombre': "",
#            'fecha': "",
#            'entregado': True
#        },
#        {
#            'nombre': "",
#            'fecha': "",
#            'entregado': True
#        },
#        {
#            'nombre': "",
#            'fecha': "",
#            'entregado': True
#        },
#    ]
#
#    year = 2000
#
#    month = 10
#
#    day = 21
#
#    entregable1 = Entregable(
#
#        nombre="Walter",
#
#        fecha_de_entrega=datetime.date(year=year, month=month, day=day),  # date year month day
#
#        entregado=True
#    )
#    entregable1.save()
#
#    contexto = {
#        'entregable': entregable1
#    }

#    return render(request, 'AppCoder/entregable.html', contexto)

def estudiante_formulario(request):

    if request.method == 'POST':
        mi_formulario = EstudianteFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            estudiante1 = Estudiantes(nombre=data.get('nombre'), apellido=data.get('apellido'), email=data.get('email'))
            estudiante1.save()

            return redirect('AppCoderEstudianteFormulario')

    estudiantes = Estudiantes.objects.all()

    contexto = {
        'form': EstudianteFormulario(),
        'estudiantes': estudiantes
    }

    return render(request, 'Appcoder/estudiante_formulario.html', contexto)

def busqueda_estudiante_post(request):

    nombre = request.GET.get('nombre')

    apellido = request.GET.get('apellido')

    email = request.GET.get('email')

    estudiantes = Estudiantes.objects.filter(nombre__icontains= nombre)

    contexto = {

        'estudiantes' : estudiantes

    }

    return render(request, 'Appcoder/estudiante_filtrado.html', contexto)

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
            profesor1.save()

            return redirect('AppCoderProfesorFormulario')

    profesores = Profesor.objects.all()

    contexto = {
        'form': EstudianteFormulario(),
        'profesores': profesores
    }

    return render(request, 'Appcoder/profesor_formulario.html', contexto)

def busqueda_profesor_post(request):

    nombre = request.GET.get('nombre')

    apellido = request.GET.get('apellido')

    email = request.GET.get('email')

    profesores = Profesor.objects.filter(nombre__icontains= nombre)

    contexto = {

        'profesores' : profesores

    }

    return render(request, 'Appcoder/profesor_filtrado.html', contexto)

def busqueda_profesor(request):

    contexto = {
        'form': BusquedaProfesorFormulario()
    }

    return render(request, 'AppCoder/busqueda_profesor.html', contexto)