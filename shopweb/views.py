from django.shortcuts import render
from products.models import Product
def home(request):
     products = Product.objects.all().filter(is_available=True).order_by('created_date')



    context = {
        'products': products,
       
    }
    return render(request, 'index.html',context)

def Products(request):
    return render(request, 'products.html')
def cart(request):
    return render(request, 'cart.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
