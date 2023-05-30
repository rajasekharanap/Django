from django.shortcuts import render, get_object_or_404
from .models import Product,Category
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def display_products(request,c_slug=None):
    c_page = None
    products_list = None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        products_list=Product.objects.all().filter(available=True)
    pagi=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products = pagi.page(page)
    except(EmptyPage,InvalidPage):
        products=pagi.page(pagi.num_pages)
    return render(request,'categories.html',{'product_categories':c_page,'allproducts':products})


def product(request,c_slug,p_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=p_slug)
    except Exception as e:
        raise e
    return render(request,'products.html',{'prodkey':product})

