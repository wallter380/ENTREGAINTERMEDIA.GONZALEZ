from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name='AppCoderInicio'),
   #path('curso/', curso, name='AppCoderCurso'),
   #path('entregable/', entregable, name='AppCoderEntregable'),
    path('curso_formulario/', curso_formulario, name='AppCoderCursoFormulario'),
    path('busqueda_camada/', busqueda_camada, name='AppCoderBusquedaCamada'),
    path('busqueda_camada_post/', busqueda_camada_post, name='AppCoderBusquedaCamadaPost'),
    path('estudiante_formulario/', estudiante_formulario, name='AppCoderEstudianteFormulario'),
    path('busqueda_estudiante/', busqueda_estudiante, name='AppCoderBusquedaEstudiante'),
    path('busqueda_estudiante_post/', busqueda_estudiante_post, name='AppCoderBusquedaEstudiantePost'),
    path('profesor_formulario/', profesor_formulario, name='AppCoderProfesorFormulario'),
    path('busqueda_profesor/', busqueda_profesor, name='AppCoderBusquedaProfesor'),
    path('busqueda_profesor_post/', busqueda_profesor_post, name='AppCoderBusquedaProfesorPost')
]
