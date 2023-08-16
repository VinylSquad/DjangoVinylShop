from django.urls import path
from . import views
from .views import search_view

urlpatterns = [
    
    # Store main page
    path('', views.store, name='store'),
    
    # Individual product page
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),
    
    # Individual category page
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),


    path('search/', search_view, name='search_view'),


    
    
    
]