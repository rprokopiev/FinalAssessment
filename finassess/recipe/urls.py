from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('recipe/<int:pk>/', views.recipe_detail_view, name='recipe_detail'),
    path('registration/', views.registration_view, name='registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_recipe/', views.add_recipe_view, name='add_recipe'),
    path('add_edit/<int:pk>/', views.edit_recipe_view, name='edit_recipe_view'),
    path('recipes/', views.recipe_detail_view, name='recipe_list'),
    path('categories/', views.category_list_view, name='category_list'),
]   