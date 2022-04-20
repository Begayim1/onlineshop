# Generated by Django 3.1 on 2022-04-19 12:08

import ckeditor.fields
import colorful.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, unique=True)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
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
                ('link_w', models.CharField(blank=True, max_length=150, null=True)),
                ('account_t', models.CharField(blank=True, max_length=55, null=True)),
                ('account_in', models.CharField(blank=True, max_length=55, null=True)),
                ('email', models.CharField(blank=True, max_length=55, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=55)),
                ('answer', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ListOfReferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('num', models.CharField(max_length=55)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('return_call', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=55)),
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
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=800, null=True)),
                ('article', models.CharField(max_length=55)),
                ('fabric', models.CharField(max_length=55)),
                ('material', models.CharField(max_length=55)),
                ('quantity_in_line', models.PositiveSmallIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('old_price', models.PositiveIntegerField(blank=True, null=True)),
                ('size_for_product', models.CharField(blank=True, max_length=55, null=True)),
                ('hit_of_sales', models.BooleanField(default=False)),
                ('new', models.BooleanField(default=True)),
                ('favorite', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
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
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='main.product', verbose_name='Product')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('color', colorful.fields.RGBColorField()),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='color', to='main.product', verbose_name='Product')),
            ],
        ),
    ]
