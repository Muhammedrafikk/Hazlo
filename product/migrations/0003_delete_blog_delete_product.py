# Generated by Django 5.0.1 on 2024-01-16 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
