# Generated by Django 4.2 on 2024-09-19 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=250, verbose_name='Category_name:')),
                ('category_slug', models.SlugField(max_length=250, verbose_name='Slug:')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=250, verbose_name='Room_name:')),
                ('room_slug', models.SlugField(max_length=250, verbose_name='Slug:')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=255, verbose_name='Hotel name:')),
                ('hotel_phone', models.IntegerField(verbose_name='Phone number:')),
                ('adress', models.CharField(max_length=255, verbose_name='Adress:')),
                ('lokatsia', models.CharField(max_length=255, verbose_name='Lokatsia:')),
                ('price', models.IntegerField(verbose_name='price:')),
                ('image1', models.ImageField(upload_to='', verbose_name='Image_1:')),
                ('image2', models.ImageField(upload_to='', verbose_name='Image_2:')),
                ('image3', models.ImageField(upload_to='', verbose_name='Image_3:')),
                ('descriptions', models.TextField(verbose_name='Descriptions:')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.category')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.room')),
            ],
        ),
    ]
