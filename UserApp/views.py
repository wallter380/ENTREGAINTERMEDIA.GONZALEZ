from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
from UserApp.forms import UserRegisterForm


def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            data = form.cleaned_data

            usuario = data.get('username')

            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:

                login(request, user)

                return render(request, 'User/inicio_sesion.html')

            else:

                return render(request, 'User/mens_verificar.html')

        else:

            return render(request, 'User/inicio_fallida.html')

        #return redirect('AppCoderInicio')

    contexto = {

        'form': AuthenticationForm(),

        'nombre_form': 'Login'
    }
    return render(request, 'User/login.html', contexto)

def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return render(request, 'User/user_registrado.html')

        else:

            return render(request, 'User/user_no_registrado.html')

    contexto = {

        'form': UserCreationForm(),

        'form': UserRegisterForm(),

        'nombre_form': 'Registro'
    }

    return render(request, 'User/login.html', contexto)