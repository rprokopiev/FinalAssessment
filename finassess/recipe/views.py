from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category
from random import choice


def home(request):
    test = "HOME TEST"
    return render(request, 'recipe/home.html', context={'test': test})


def add_recipe(request):
    test = "ADD RECIPE TEST"
    return render(request, 'recipe/add_recipe.html', context={'test': test})


def login(request):
    test = "LOGIN TEST"
    return render(request, 'recipe/login.html', context={'test': test})


def logout(request):
    test = "LOGOUT TEST"
    return render(request, 'recipe/logout.html', context={'test': test})


def recipe_detail(request):
    test = "recipe_detail TEST"
    return render(request, 'recipe/recipe_detail.html', context={'test': test})


def registration(request):
    test = "REGISTRATION TEST"
    return render(request, 'recipe/registration.html', context={'test': test})
