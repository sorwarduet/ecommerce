# Generated by Django 3.0.11 on 2020-12-17 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
