from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    def clean(self):
        # self.cleaned_data['username'] = 'amenotijaraka'
        data = self.cleaned_data

        username = data.get('username')
        first_name = data.get('first_name')

        if len(username) < 5:
            self.add_error(
                'username',
                'nome de usuario muito curto',
            )

        if User.objects.filter(username=username).exists():
            self.add_error(
                'username',
                'nome de usuário já existente'
            )
        
        if len(first_name) < 5:
            self.add_error(
                'first_name',
                'primeiro nome muito curto'
            )


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
