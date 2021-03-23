#from django.forms import ModelForm, HiddenInput, IntegerField, CharField
from django import forms

from .models import Ingredient, Cocktail, Recipe

class IngredientForm(forms.ModelForm):
    """Form for adding ingredients"""
    class Meta:
        model = Ingredient
        fields = ['name','description']
        # labels = {'name': ''}

class RecipeForm(forms.ModelForm):
    """Form for adding ingredients"""

    class Meta:
        model = Recipe
        fields = ['ingredient','quantity']


class CocktailForm(forms.ModelForm):
    """Form for adding ingredients"""

    class Meta:
        model = Cocktail
        fields = ['name','description','steps']
        # labels = {'name': ''}
