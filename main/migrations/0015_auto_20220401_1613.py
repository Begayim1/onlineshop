# Generated by Django 3.1 on 2022-04-01 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_help_imagehelp'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagehelp',
            name='help',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='main.help'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagehelp',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
