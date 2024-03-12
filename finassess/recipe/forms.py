from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Recipe, Category


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Имя пользователя', 
            'email': 'Электронная почта', 
            'password1': 'Пароль', 
            'password2': 'Повторите пароль'
        }


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            'username': 'Имя пользователя', 
            'password': 'Пароль', 
        }


class RecipeForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'steps', 'cooking_time', 'image', 'categories']
        labels = {
            'title': 'Название', 
            'description': 'Описание', 
            'steps': 'Шаги приготовлеия', 
            'cooking_time': 'Время приготовления',
            'image': 'Картинка', 
            'categories': 'Категория',
        }