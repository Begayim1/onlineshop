# Generated by Django 3.1 on 2022-04-05 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]