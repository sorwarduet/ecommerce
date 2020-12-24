from django.urls import path

from ecommerce.carts.views import (
    cart_home,
    card_update,
    checkout_home


)

app_name = "search"
urlpatterns = [
    path("", cart_home, name="cart"),
    path('update/', card_update, name='update'),
    path('checkout/', checkout_home, name='checkout')

]
