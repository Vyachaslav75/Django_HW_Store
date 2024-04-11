from django.core.management.base import BaseCommand

from myapp.models import Order
from myapp.models import User
from myapp.models import Product


class Command(BaseCommand):
    help = "Get order."

    def handle(self, *args, **kwargs):
        order = Order.objects.filter(pk=1).first()
        print(order.customer.name, order.products.all())
        # order.save()
        # self.stdout.write(f'{product}')
