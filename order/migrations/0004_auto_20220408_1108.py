# Generated by Django 3.1 on 2022-04-08 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20220408_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Decorated', 'Decorated'), ('Cancelled', 'Cancelled')], max_length=55, null=True),
        ),
    ]
