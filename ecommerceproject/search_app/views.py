from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
from django.http import HttpResponse


def SearchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {'query': query, 'products': products})
