from django.shortcuts import render

from . models import Category, Product

from django.shortcuts import get_object_or_404

# Create your views here.


def store(request):

    all_products = Product.objects.all().order_by('?')

    context = {'all_products': all_products}

    return render(request, 'store/store.html', context)


def categories(request):

    all_categories = Category.objects.all()

    return {'all_categories': all_categories}

    # After that go to context processor in setting.py/TEMPLATES and add your views


def list_category(request, category_slug=None):

    category = get_object_or_404(Category, slug=category_slug)

    products = Product.objects.filter(category=category)

    return render(request, 'store/list-category.html', {'category': category, 'products': products})


def product_info(request, product_slug):

    product = get_object_or_404(Product, slug=product_slug)

    context = {'product': product}

    return render(request, 'store/product-info.html', context)


def search_view(request):
    query = request.GET.get('query')
    results = []

    if query:
        results = Product.objects.filter(artist__icontains=query)  # Replace 'title' with the field you want to search

    context = {
        'query': query,
        'results': results,
    }

    return render(request, 'store/search_results.html', context)


def error_404(request, exception):
    
    return render(request, '404.html')