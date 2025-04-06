from django.shortcuts import render

from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.all() # Fetch all products from the database
    return render(request, 'home.html',{'products': products}) # Pass the products to the template
