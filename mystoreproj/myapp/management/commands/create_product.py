from django.core.management.base import BaseCommand

from myapp.models import Product
class Command(BaseCommand):
    help = "Create product."
    def handle(self, *args, **kwargs):
        product = Product(prod_name='Knife', description='very shark', price=100, prod_count=100)
        product.save()
        self.stdout.write(f'{product}')