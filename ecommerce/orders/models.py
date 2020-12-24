from django.db import models
from django.db.models.signals import post_save
from ecommerce.carts.models import Cart
from ecommerce.orders.utils import generate_order_id
from math import fsum
# Create your models here.


ORDER_STATUS = (
    ('created', 'Created'),
    ('paid', "Paid"),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded')
)


class Order(models.Model):
    order_id = models.CharField(max_length=120, blank=True, editable=False)

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='created', choices=ORDER_STATUS)
    shipping_total = models.DecimalField(max_digits=20, decimal_places=2, default=5.0)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)

    def __str__(self):
        return str(self.order_id)

    def update_total(self):
        cart_total = self.cart.total
        shipping_total = self.shipping_total
        new_total = fsum([cart_total, shipping_total])
        self.total = new_total
        self.save()
        return new_total

    def save(self, *args, **kwargs):
        self.order_id = generate_order_id()
        super(Order, self).save(*args, **kwargs)


def post_save_cart_total(sender, instance, created,  *args, **kwargs):
    print('cart_total called')
    if not created:
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart__id=cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()


post_save.connect(post_save_cart_total, sender=Cart)


def post_save_order(sender, instance, created, *args, **kwargs):
    print("Order function called")
    if created:
        instance.update_total()


post_save.connect(post_save_order, sender=Order)
