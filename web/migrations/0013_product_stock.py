# Generated by Django 5.0.1 on 2024-01-17 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_alter_blog_paraph_alter_product_paraph_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.BooleanField(default=False),
        ),
    ]
