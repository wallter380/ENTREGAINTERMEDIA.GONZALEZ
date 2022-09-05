from django import forms


class CursoFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)

    camada = forms.IntegerField()

class BusquedaCamadaFormulario(forms.Form):

    camada = forms.IntegerField()

class EstudianteFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)

    apellido = forms.CharField(max_length=40)

    email = forms.EmailField()

class BusquedaEstudianteFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)

    apellido = forms.CharField(max_length=40)

    email = forms.EmailField()

class BusquedaProfesorFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)