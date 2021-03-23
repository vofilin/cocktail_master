# Generated by Django 3.0.8 on 2020-07-17 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0002_ingredient_steps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='steps',
        ),
        migrations.AddField(
            model_name='cocktail',
            name='steps',
            field=models.TextField(default='Steps'),
            preserve_default=False,
        ),
    ]