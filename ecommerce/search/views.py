from django.shortcuts import render
from ecommerce.products.models import Product
from django.views.generic import ListView


class ProductSearchView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'search/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict =request.GET
        query =method_dict.get('q', None)
        print(query)

        if query is not None:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


