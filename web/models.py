from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from PIL import Image

# Create your models here.

class Product(models.Model):
    image = models.ImageField(
        upload_to="products/img",
        help_text="The recommended size is 600x300 pixels.",
    )
    image_width = models.PositiveIntegerField(null=True, blank=True, editable=False)
    image_height = models.PositiveIntegerField(null=True, blank=True, editable=False)

    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    paraph = models.TextField(unique=True, blank=True, null=True)
    price = models.IntegerField(unique=True, blank=True, null=True)
    
    content = HTMLField(unique=True, blank=True, null=True)   
    stock = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            width, height = img.size
            self.image_width = width
            self.image_height = height
            img.close()
            self.save(update_fields=['image_width', 'image_height'])

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ("Products")
        verbose_name_plural = ("Products")

    def get_absolute_url(self):
        return reverse('web:product_details', kwargs={'slug': self.slug})
   
    
class ProductImage(models.Model):
    product_pro = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()


class Blog(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    paraph = models.TextField(unique=True, blank=True, null=True)

    content = HTMLField(unique=True, blank=True, null=True)
    stock = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ("Updates")
        verbose_name_plural = ("Updates")

    def get_absolute_url(self):
        return reverse('web:blog_details', kwargs={'slug': self.slug})
    

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contact")
    

