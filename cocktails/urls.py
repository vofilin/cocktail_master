"""Defines URL patterns for cocktails."""

from django.urls import path
from . import views

app_name = 'cocktails'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that displays all ingredients
    path('ingredients/', views.ingredients, name='ingredients'),
    # Detail page for an Ingredient.
    path('ingredients/<int:ingredient_id>/',
         views.ingredient, name='ingredient'),
    # Page for adding new ingredient.
    path('ingredients/new_ingredient/',
         views.new_ingredient, name='new_ingredient'),
    # Page for editing ingredient.
    path('ingredients/<int:ingredient_id>/edit',
         views.edit_ingredient, name='edit_ingredient'),
    # Page for deleting ingredient.
    path('ingredients/<int:ingredient_id>/delete',
         views.delete_ingredient, name='delete_ingredient'),

    # Page that displays all cocktails
    path('cocktails/', views.cocktails, name='cocktails'),
    # Detail page for a Cocktail.
    path('cocktails/<int:cocktail_id>/', views.cocktail, name='cocktail'),
    # Page for adding new cocktail.
    path('cocktails/new_cocktail/', views.new_cocktail, name='new_cocktail'),
    # Page for editing ingredient.
    path('cocktails/<int:cocktail_id>/edit', views.edit_cocktail,
         name='edit_cocktail'),
    # Page for deleting ingredient.
    path('cocktails/<int:cocktail_id>/delete', views.delete_cocktail,
         name='delete_cocktail'),

]
