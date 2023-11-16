from django.shortcuts import render, get_object_or_404

from .models import Category, Product

def categories(request):
    return{
        'categories': Category.objects.all()
    }

def product_all(request):
    products = Product.objects.filter(in_stock=True)
    return render(request, 'store/home.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug = category_slug)
    products = Product.objects.filter(category=category).filter(in_stock=True)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})



def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})
# Create your views here.
