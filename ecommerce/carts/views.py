from django.shortcuts import render, redirect
from .models import Cart
from ecommerce.products.models import Product


# Create your views here.


# def cart_create(user=None):
#     cert_obj = Cart.objects.create(user=None)
#     print('Cart New Create')
#     return cert_obj

def cart_home(request):
    # print(request.session)
    # print(dir(request.session))
    # print(request.session.session_key)
    # print(request.session.set_expiry(300))
    # request.session['name'] = 'Md. Sorwar alam'
    # print(request.session.get('name'))
    # request.session['cart_id'] = 12

    cart_obj, new_obj = Cart.objects.new_or_get(request)
    context = {
        'cart': cart_obj
    }

    return render(request, 'carts/home.html', context)


def card_update(request):
    product_id = request.POST.get('product_id')
    try:
        product_obj = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        print('Show message')
        return redirect('cart:cart')

    cart_obj, new_obj = Cart.objects.new_or_get(request)

    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj)
    request.session['cart_items'] = cart_obj.products.count()
    return redirect('cart:cart')
