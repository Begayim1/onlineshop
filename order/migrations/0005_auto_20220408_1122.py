# Generated by Django 3.1 on 2022-04-08 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20220408_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]
