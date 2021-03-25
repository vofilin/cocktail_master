#from django.forms import ModelForm, HiddenInput, IntegerField, CharField
from django import forms

from .models import Ingredient, Cocktail, Recipe

class IngredientForm(forms.ModelForm):
    """Form for adding ingredients"""
    class Meta:
        model = Ingredient
        fields = ['name','description']

class RecipeForm(forms.ModelForm):
    """Form for adding ingredients"""

    class Meta:
        model = Recipe
        fields = ['ingredient','quantity']

    # Change default order for ingredient field to sorting by ingredient name
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['ingredient'].queryset = self.fields['ingredient'].queryset.order_by('name')

    def clean(self):
        cleaned_data = super().clean()

        # Check that quantity is gt 0
        if cleaned_data["quantity"] <= 0:
            self.add_error(None, f"Quantity must be greater then zero")

        return cleaned_data


class CocktailForm(forms.ModelForm):
    """Form for adding ingredients"""

    class Meta:
        model = Cocktail
        fields = ['name','description','steps']
