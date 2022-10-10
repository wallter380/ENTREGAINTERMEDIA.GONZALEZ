from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from UserApp.models import Avatar


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    last_name = forms.CharField()

    class Meta:

        model = User

        fields = ('username', 'email', 'last_name')


class AvatarForm(forms.ModelForm):

    class Meta:

        model = Avatar

        fields = "__all__"












