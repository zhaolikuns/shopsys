from django.shortcuts import render, get_object_or_404

from .models import Category, Product

# Create your views here.

def index(request, templates_name):
    page_title = '产品分类目录'
    return render(request, templates_name, locals())

def show_category(request, category_slug, templates_name):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render(request, templates_name, locals())

def show_product(request, product_slug, templates_name):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    return render(request, templates_name, locals())