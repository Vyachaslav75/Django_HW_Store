from django.core.management.base import BaseCommand

from myapp.models import Order
from myapp.models import User
from myapp.models import Product


class Command(BaseCommand):
    help = "Get order."

    def handle(self, *args, **kwargs):
        user = User.objects.filter(pk=7).first()
        orders = Order.objects.filter(customer=user).all()   #first()
        prods = set()
        print(len(orders))
        for order in orders:
            for prod in order.products.all():
                prods.add(prod.name())
                print(prod.name())
            print(prods)
        print(order.customer.name, order.products.all())
        # order.save()
        # self.stdout.write(f'{product}')
