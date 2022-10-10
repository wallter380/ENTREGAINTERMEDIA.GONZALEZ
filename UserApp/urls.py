from django.contrib.auth.views import LogoutView
from django.urls import path

from UserApp.views import *

urlpatterns = [
    path('login/', login_request, name='UserAppLogin'),
    path('registro/', register, name='UserAppRegister'),
    path('logout/', LogoutView.as_view(template_name='User/logout.html'), name='UserAppLogout'),
    path('editar/', editar_usuario, name='UserAppEditar'),
    path('avatar/', upload_avatar, name='UserAppAvatar')
]
