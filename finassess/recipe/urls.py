from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
]