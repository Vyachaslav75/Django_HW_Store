from django.core.management.base import BaseCommand

from myapp.models import Product


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(prod_name='Scissors', description='shark', price=120, prod_count=80)
        product.save()
        self.stdout.write(f'{product}')
