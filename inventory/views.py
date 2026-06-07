from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request, "home.html")


def add_item(request):
    return render(request, "add_item.html")


def about(request):
    return render(request, "about.html")

def pricing(request):
    return render(request, "pricing.html")





def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # 🔐 Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # ✅ Log user in (this creates session)
            login(request, user)

            return redirect("dashboard")  # or home page
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "registration/login.html")

def logout_view(request):
    logout(request)
    return redirect("login") 

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()  # creates the user in DB
            messages.success(request, "Account created successfully!")
            return redirect("login")  # send user to login page
        else:
            messages.error(request, "Please correct the errors below.")

    else:
        form = UserCreationForm()

    return render(request, "registration.html", {"form": form})


def registration(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # 1. Validate passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("registration")

        # 2. Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("registration")

        # 3. Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use")
            return redirect("registration")

        # 4. Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # 5. Split full name into first & last name
        name_parts = full_name.split(" ", 1)
        user.first_name = name_parts[0]

        if len(name_parts) > 1:
            user.last_name = name_parts[1]

        user.save()

        messages.success(request, "Account created successfully!")
        return redirect("login")

    return render(request, "registration.html")

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


@login_required(login_url='login')
def dashboard(request):
    return render(request, "dashboard.html")


class CustomLoginView(LoginView):
    template_name = 'login.html'