from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    def clean(self):
        data = self.cleaned_data
        username = data.get('username')
        first_name = data.get('first_name')

        if len(username) < 10:
            self.add_error(
                'username',
                'nome de usuario muito curto'
            )

        if len(first_name) < 10:
            self.add_error(
                'first_name',
                'nome muito curto'
            )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')
