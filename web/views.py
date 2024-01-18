from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .forms import ContactForm

from . models import Blog
from . models import Product

def index(request):
    products = Product.objects.all() 
    blogs = Blog.objects.all() 

    context = {
        "products":products,
        "blogs":blogs,
    }
    return render(request, "web/index.html", context)


def about(request):
    return render(request, "web/about.html")


def product(request):
    products = Product.objects.all() 

    context = {
        "products":products,
    }
    return render(request, "web/product.html",context)


def product_details(request,slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        "product":product,
    }
    return render(request, "web/product_details.html",context)


def blog(request):
    blogs = Blog.objects.all() 

    context = {
        "blogs":blogs,
    }
    return render(request, "web/blog.html",context)


def blog_details(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    context = {
        'blog': blog,
    }
    return render(request, "web/blog_details.html", context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
            
    else:
        form = ContactForm()

    return render(request, 'web/contact.html', {'form': form})

