# Generated by Django 3.1 on 2022-03-31 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220331_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]