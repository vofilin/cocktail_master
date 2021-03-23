from django.contrib import admin
from .models import Ingredient, Cocktail, Recipe

admin.site.register(Ingredient)
admin.site.register(Cocktail)
admin.site.register(Recipe)
