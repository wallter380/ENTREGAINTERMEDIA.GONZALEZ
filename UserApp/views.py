from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from UserApp.forms import UserRegisterForm, AvatarForm


# Create your views here.
from UserApp.models import Avatar


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

    contexto = {

        'form': AuthenticationForm(),

        'nombre_form': 'Login'
    }
    return render(request, 'User/login.html', contexto)

def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return render(request, 'User/user_registrado.html')

        else:

            return render(request, 'User/user_no_registrado.html')

    contexto = {

        'form': UserRegisterForm(),

        'nombre_form': 'Registro'
    }

    return render(request, 'User/login.html', contexto)

# Editar usuario propio
@login_required

def editar_usuario(request):

    usuario = request.user

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            usuario.username = data.get('username')
            usuario.email = data.get('email')
            usuario.last_name = data.get('last_name')

            usuario.save()

            return render(request, 'User/user_registrado.html')

        else:

            return render(request, 'User/user_no_registrado.html')

    contexto = {

        'form': UserRegisterForm(

            initial={

                'username': usuario.username,
                'email': usuario.email,
                'last_name': usuario.last_name

            }),

        'nombre_form': 'Registro'
    }

    return render(request, 'User/login.html', contexto)

@login_required
def upload_avatar(request):
    if request.method == "POST":

        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            avatar = Avatar.objects.filter(user=data.get("usuario"))

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()

            else:
                avatar = Avatar(user=data.get("user"), imagen=data.get("imagen"))
                avatar.save()

        return redirect("AppCoderInicio")

    contexto = {
        "form": AvatarForm(),
        'boton_envio': 'Crear'
    }
    return render(request, "User/avatar.html", contexto)