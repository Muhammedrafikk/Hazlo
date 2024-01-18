# Generated by Django 5.0.1 on 2024-01-16 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('paraph', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product',
            },
        ),
    ]