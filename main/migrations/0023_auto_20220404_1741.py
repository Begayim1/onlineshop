# Generated by Django 3.1 on 2022-04-04 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_remove_color_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='color',
            options={},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]