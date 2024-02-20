from django.core.management.base import BaseCommand

from myapp.models import Order
from myapp.models import User
from myapp.models import Product
class Command(BaseCommand):
    help = "Create order."
    def handle(self, *args, **kwargs):
        user = User.objects.filter(pk=1).first()
        product = Product.objects.filter(pk=1).first()
        order = Order(customer=user, products.add(product.prod_name), total_price=product.price)
        order.save()
        #self.stdout.write(f'{product}')