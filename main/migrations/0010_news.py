# Generated by Django 3.1 on 2022-03-31 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20220331_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.TextField(blank=True, max_length=400)),
                ('image', models.ImageField(upload_to='images/Y%/M%/H%')),
            ],
        ),
    ]
