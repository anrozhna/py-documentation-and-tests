# Generated by Django 4.1 on 2024-06-12 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(
                blank=True, related_name="movies", to="cinema.actor"
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(
                blank=True, related_name="movies", to="cinema.genre"
            ),
        ),
    ]
