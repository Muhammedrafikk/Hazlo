from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    path('product/', views.product, name='product'),
    path('product/<slug:slug>/', views.product_details, name='product_details'),

    path('blogs/',views.blog, name='blog'),
    path('blogs/<slug:slug>/', views.blog_details, name='blog_details'),
]