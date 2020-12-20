from django.urls import path

from ecommerce.carts.views import (
    cart_home,
    card_update


)

app_name = "search"
urlpatterns = [
    path("", cart_home, name="cart"),
    path('update/', card_update, name='update')

]
