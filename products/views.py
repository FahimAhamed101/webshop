
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product,Variation
from category.models import Category
from carts.models import CartItem
from django.db.models import Q

from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

from django.contrib import messages



def store(request, category_slug=None):
 
    categories = None
    products = None

  
    
    
       
        
    if category_slug != None:
        
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
        
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
     
        
    }
    return render(request, 'products.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e

    
    # Get the reviews
   

    # Get the product gallery


    context = {
        'single_product': single_product,
        'in_cart'       : in_cart,
        
        
        
    }
    return render(request, 'product_detail.html', context)


def search(request,products=None,product_count=0):
 
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    
    if 'size' in request.GET:
    
        size=request.GET['size']
     
        print(size)
       
       
        if size:
            sizeoption=Variation.objects.filter(sizeoption=size).first()
            print(sizeoption)
            products = Product.objects.filter(variation=sizeoption)
            product_count = products.count()
       
    context = {
        'products': products,
        'product_count': product_count,
       
       

    }
    return render(request, 'store/products.html', context)