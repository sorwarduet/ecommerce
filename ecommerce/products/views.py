from django.shortcuts import render
from django.views.generic import ListView, DetailView

from ecommerce.products.models import Product
# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'

    def get_queryset(self,*args, **kwargs):
        return Product.objects.active()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'
