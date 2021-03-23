from django.db import models
from django.db.models.functions import Length

models.CharField.register_lookup(Length)

class Ingredient(models.Model):
    """Ingredient for cocktails."""
    name = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        constraints = [
            models.CheckConstraint(name="ingredient_name_not_empty",
                check=models.Q(name__length__gt=0)),
            models.UniqueConstraint(name="ingredient_name_unique", fields=["name"]),
        ]

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Cocktail(models.Model):
    """Cocktail model."""
    name = models.CharField(max_length=30)
    description = models.TextField()
    steps = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    ingredients = models.ManyToManyField(
        Ingredient,
        through='Recipe',
        through_fields=('cocktail', 'ingredient'),
    )

    class Meta:
        constraints = [
            models.CheckConstraint(name="cocktail_name_not_empty",
                check=models.Q(name__length__gt=0)),
            models.UniqueConstraint(name="cocktail_name_unique", fields=["name"]),
        ]

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Recipe(models.Model):
    """Recipe model."""
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.quantity} ml of {self.ingredient}"
