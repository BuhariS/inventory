from django.urls import path
from . import views

#path("products/", views.products, name="products")

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_item, name="add_item"),
    path("products/", views.products, name="products"),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path("logout/", views.logout_view, name="logout"), 
]