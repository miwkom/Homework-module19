from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Введите логин:', max_length=100)
    password = forms.CharField(label='Введите пароль:', min_length=8)
    repeat_password = forms.CharField(label='Повторите пароль:', min_length=8)
    age = forms.IntegerField(label='Введите свой возраст:', max_value=999)