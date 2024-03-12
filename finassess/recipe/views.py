from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from .models import Recipe, Category
from random import choice
from .forms import RegistrationForm, LoginForm, RecipeForm


def home(request):
    recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'recipe/home.html', {'recipes': recipes})


def category_list_view(request):
    categories = Category.objects.all()
    return render(request, 'recipe/category_list.html', {'categories': categories})


def add_recipe_view(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'recipe/add_recipe.html', {'form': form})


def edit_recipe_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe/edit_recipe.html', {'form': form, 'recipe': recipe})


def recipe_detail_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'recipe/registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'recipe/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def recipe_list_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/recipe_list.html', {'recipes': recipes})