from django.urls import path
from . import views

#path("products/", views.products, name="products")

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_item, name="add_item"),
    path("products/", views.products, name="products"),
    path('login/', views.CustomLoginView.as_view(), name='login'),
]