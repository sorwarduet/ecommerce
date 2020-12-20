# Generated by Django 3.0.11 on 2020-12-17 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=30.15, max_digits=20),
        ),
    ]