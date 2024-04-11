from django.core.management.base import BaseCommand

from myapp.models import Order
from myapp.models import User
from myapp.models import Product


class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        user = User.objects.filter(pk=1).first()
        product1 = Product.objects.filter(pk=1).first()
        product2 = Product.objects.filter(pk=2).first()
        # order = Order(customer=user, products.add(product), total_price=product.price)
        print(product1)
        price = product1.price + product2.price
        order = Order.objects.create(customer=user, total_price=price)
        order.products.add(product1, product2)
        # order.save()
        # self.stdout.write(f'{product}')
