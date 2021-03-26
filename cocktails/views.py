from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Cocktail, Ingredient, Recipe
from .forms import IngredientForm, RecipeForm, CocktailForm

def index(request):
    """The home page for Cocktails."""
    return render(request, 'cocktails/index.html')


def ingredients(request):
    """Show all ingredients"""
    query = request.GET.get('q')
    if query:
        ingredients = Ingredient.objects.filter(name__icontains=query).order_by('name')
    else:
        ingredients = Ingredient.objects.order_by('name')

    paginator = Paginator(ingredients, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'cocktails/ingredients.html', context)


def ingredient(request, ingredient_id):
    """Show a single ingredient."""
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    context = {'ingredient': ingredient, 'description':ingredient.description}
    return render(request, 'cocktails/ingredient.html', context)


def new_ingredient(request):
    """Add new ingredient."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = IngredientForm()
    else:
        # POST data submitted; process data.
        form = IngredientForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cocktails:ingredients')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'cocktails/new_ingredient.html', context)


def edit_ingredient(request, ingredient_id):
    """Edit ingredient."""
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = IngredientForm(instance=ingredient)
    else:
        # POST data submitted; process data.
        form = IngredientForm(instance=ingredient, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cocktails:ingredient', ingredient_id=ingredient_id)

    # Display a blank or invalid form.
    context = {'ingredient': ingredient, 'form': form}
    return render(request, 'cocktails/edit_ingredient.html', context)


def delete_ingredient(request, ingredient_id):
    """Delete ingredient."""
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    cocktails = Cocktail.objects.filter(ingredients__id=ingredient_id)

    if request.method == 'POST':
        ingredient.delete()
        return redirect('cocktails:ingredients')

    context = {'ingredient': ingredient, 'cocktails': cocktails}
    return render(request, 'cocktails/delete_ingredient.html', context)


def cocktails(request):
    """Show all cocktails"""
    query = request.GET.get('q')
    if query:
        cocktails = Cocktail.objects.filter(
            Q(name__icontains=query) |
            Q(ingredients__name__icontains=query)).order_by('name').distinct()
    else:
        cocktails = Cocktail.objects.order_by('name')

    paginator = Paginator(cocktails, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'cocktails/cocktails.html', context)


def cocktail(request, cocktail_id):
    """Show a single cocktail."""
    cocktail = get_object_or_404(Cocktail, id=cocktail_id)
    ingredients = Recipe.objects.filter(cocktail=cocktail)
    context = {'cocktail': cocktail,
        'description':cocktail.description,
        'ingredients':ingredients,
        'steps':cocktail.steps}
    return render(request, 'cocktails/cocktail.html', context)


def new_cocktail(request):
    """Add a new cocktail."""

    IngredientsFormset = modelformset_factory(Recipe, form = RecipeForm)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CocktailForm()
        formset = IngredientsFormset(queryset=Recipe.objects.none())
    else:
        # POST data submitted; process data.
        form = CocktailForm(data=request.POST)
        formset = IngredientsFormset(request.POST)
        if form.is_valid() and formset.is_valid():
            cocktail = form.save()
            ingredients = formset.save(commit=False)
            for ingredient in ingredients:
                ingredient.cocktail = cocktail
                ingredient.save()
            return redirect('cocktails:cocktails')

    # Display a blank or invalid form.
    context = {'form': form, 'formset': formset}
    return render(request, 'cocktails/new_cocktail.html', context)


def edit_cocktail(request, cocktail_id):
    """Edit cocktail."""
    cocktail = get_object_or_404(Cocktail, id=cocktail_id)
    IngredientsFormset = modelformset_factory(Recipe, form = RecipeForm)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CocktailForm(instance=cocktail)
        formset = IngredientsFormset(queryset=Recipe.objects.filter(cocktail=cocktail))
    else:
        # POST data submitted; process data.
        form = CocktailForm(instance=cocktail, data=request.POST)
        formset = IngredientsFormset(request.POST)
        if form.is_valid() and formset.is_valid():
            cocktail = form.save()
            ingredients = formset.save(commit=False)
            for ingredient in ingredients:
                ingredient.cocktail = cocktail
                ingredient.save()
            return redirect('cocktails:cocktails')

    # Display a blank or invalid form.
    context = {'cocktail': cocktail, 'form': form, 'formset': formset}
    return render(request, 'cocktails/edit_cocktail.html', context)


def delete_cocktail(request, cocktail_id):
    """Delete cocktail."""
    cocktail = get_object_or_404(Cocktail, id=cocktail_id)

    if request.method == 'POST':
        cocktail.delete()
        return redirect('cocktails:cocktails')

    context = {'cocktail': cocktail}
    return render(request, 'cocktails/delete_cocktail.html', context)
