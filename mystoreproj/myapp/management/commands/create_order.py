from django.core.management.base import BaseCommand

from myapp.models import Order
from myapp.models import User
from myapp.models import Product
from random import choice, randint


class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        # user = User.objects.filter(pk=1).first()
        # product1 = Product.objects.filter(pk=1).first()
        # product2 = Product.objects.filter(pk=2).first()
        #
        # print(product1)
        # price = product1.price + product2.price
        # order = Order.objects.create(customer=user, total_price=price)
        # order.products.add(product1, product2)

        for i in range(11):
            user_id = randint(1, 20)
            print(user_id)
            user = User.objects.filter(pk=user_id).first()
            order = Order.objects.create(customer=user, total_price=0)
            prod_count = randint(1, 11)
            for j in range(prod_count):
                prod_id = randint(1, 31)
                product = Product.objects.filter(pk=prod_id).first()
                order.products.add(product)
                print(product)
                order.total_price+=product.price
                order.save()
