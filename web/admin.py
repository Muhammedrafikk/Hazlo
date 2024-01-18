from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import ProductImage

from .models import Contact
from .models import Blog
from .models import Product

# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]
    prepopulated_fields = {'slug': ('title',)}
    list_display = ("title","image_preview" ,"price","stock")
    list_filter = ( "title","price")
    search_fields = ("title","image_preview","price","stock")

    

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img loading="lazy" src="{obj.image.url}" style="width:70px;object-fit:contain;">'
            )
        return ""

    image_preview.short_description = 'Image Preview'

    

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ("title","image_preview","stock")
    list_filter = ( "title","paraph","stock")
    search_fields = ("title","image_preview","paraph","stock")


    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img loading="lazy" src="{obj.image.url}" style="width:70px;object-fit:contain;">'
            )
        return ""

    image_preview.short_description = 'Image Preview'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email","subject","message")
    list_display = ("name", "email","subject","message")
    list_filter = ("name", "email","subject","message")
    search_fields = ("name", "email","subject","message")


