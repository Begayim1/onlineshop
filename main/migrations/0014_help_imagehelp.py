# Generated by Django 3.1 on 2022-04-01 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_publicoffer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=55)),
                ('answer', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ImageHelp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
