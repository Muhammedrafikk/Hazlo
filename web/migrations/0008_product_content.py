# Generated by Django 5.0.1 on 2024-01-16 05:52

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_product_slug_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content',
            field=tinymce.models.HTMLField(blank=True, null=True, unique=True),
        ),
    ]
