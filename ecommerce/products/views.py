from django.shortcuts import render
from django.views.generic import ListView, DetailView

from ecommerce.products.models import Product
from ecommerce.carts.models import Cart
# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'


    def get_queryset(self, *args, **kwargs):
        return Product.objects.active()



class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart_obj'] = cart_obj
        return context






