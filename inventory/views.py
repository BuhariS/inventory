from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView

# Create your views here.

def home(request):
    return render(request, "home.html")


def add_item(request):
    return render(request, "add_item.html")




class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'


@login_required
def products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products.html', context)




class CustomLoginView(LoginView):
    template_name = 'login.html'