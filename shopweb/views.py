from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def Products(request):
    return render(request, 'products.html')
def cart(request):
    return render(request, 'cart.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')