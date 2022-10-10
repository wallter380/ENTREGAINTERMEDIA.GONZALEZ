from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name='AppCoderInicio'),
    path('curso_formulario/', curso_formulario, name='AppCoderCursoFormulario'),
    path('busqueda_camada/', busqueda_camada, name='AppCoderBusquedaCamada'),
    path('busqueda_camada_post/', busqueda_camada_post, name='AppCoderBusquedaCamadaPost'),
    path('estudiante_formulario/', estudiante_formulario, name='AppCoderEstudianteFormulario'),
    path('busqueda_estudiante/', busqueda_estudiante, name='AppCoderBusquedaEstudiante'),
    path('busqueda_estudiante_post/', busqueda_estudiante_post, name='AppCoderBusquedaEstudiantePost'),
    path('profesor_formulario/', profesor_formulario, name='AppCoderProfesorFormulario'),
    path('busqueda_profesor/', busqueda_profesor, name='AppCoderBusquedaProfesor'),
    path('busqueda_profesor_post/', busqueda_profesor_post, name='AppCoderBusquedaProfesorPost'),
    path('eliminar_curso/ <int:camada>', eliminar_curso, name='AppCoderEliminarCurso'),
    path('curso_eliminado/', curso_eliminado, name='AppCoderCursoEliminado'),
    path('profesor_eliminado/', profesor_eliminado, name='AppCoderProfesorEliminado'),
    path('estudiante_eliminado/', estudiante_eliminado, name='AppCoderEstudianteEliminado'),
    path('eliminar_profesor/ <str:nombre> <str:apellido> <str:email>', eliminar_profesor, name='AppCoderEliminarProfesor'),
    path('eliminar_estudiante/ <str:nombre> <str:apellido> <str:email>', eliminar_estudiante, name='AppCoderEliminarEstudiante'),
    path('editar_curso/<int:camada>', editar_curso, name='AppCoderEditarCurso'),
    path('editar_estudiante/<str:nombre> <str:apellido> <str:email>', editar_estudiante, name='AppCoderEditarEstudiante'),
    path('editar_profesor/<str:nombre> <str:apellido> <str:email>', editar_profesor, name='AppCoderEditarProfesor'),
    path('curso_no_editar/', curso_no_editar, name='AppCoderCursoNoEditar'),
    path('estudiante_no_editar/', estudiante_no_editar, name='AppCoderEstudianteNoEditar'),
    path('profesor_no_editar/', profesor_no_editar, name='AppCoderProfesorNoEditar'),
    path('about/', about, name='AppCoderAbout')
]
