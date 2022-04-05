# Generated by Django 3.1 on 2022-04-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20220405_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='title',
        ),
        migrations.AddField(
            model_name='footer',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footer',
            name='number',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='footer',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='image_h'),
        ),
    ]
