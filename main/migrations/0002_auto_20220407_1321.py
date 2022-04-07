# Generated by Django 3.1 on 2022-04-07 07:21

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=800, null=True)),
            ],
            options={
                'verbose_name': 'AboutUs',
                'verbose_name_plural': 'AboutUss',
            },
        ),
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.TextField(blank=True, max_length=800, null=True)),
                ('image', models.ImageField(upload_to='images/Y%/M%/H%')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('image', models.ImageField(upload_to='images/Y%/M%/H%')),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='images_f')),
                ('logo_h', models.ImageField(blank=True, null=True, upload_to='image_h')),
                ('description', models.TextField(max_length=200)),
                ('num', models.CharField(max_length=55)),
                ('type', models.CharField(choices=[('WhatsApp', 'WhatsApp'), ('Telegram', 'Telegram'), ('Instagram', 'Instagram'), ('Mail', 'Mail')], max_length=55)),
                ('link_num', models.CharField(blank=True, max_length=150, null=True)),
                ('account', models.CharField(blank=True, max_length=55, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=55)),
                ('answer', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ListOfReferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('num', models.CharField(max_length=55)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Data')),
                ('return_call', models.BooleanField(default=True)),
                ('call', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=800, null=True)),
                ('image', models.ImageField(upload_to='images/Y%/M%/H%')),
            ],
        ),
        migrations.CreateModel(
            name='PublicOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=800, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReturnCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Whatsapp', 'Whatsapp'), ('Telegram', 'Telegram'), ('Number', 'Number')], max_length=55)),
                ('name', models.CharField(max_length=55)),
                ('num_user', models.CharField(max_length=55)),
                ('return_call', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='color',
            options={},
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created',
        ),
        migrations.AddField(
            model_name='color',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='color', to='main.product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='favorite',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.CreateModel(
            name='ImageUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('about_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='main.aboutus')),
            ],
        ),
        migrations.CreateModel(
            name='ImageHelp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('help', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='main.help')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(to='main.Size', verbose_name=main.models.Size),
        ),
    ]
