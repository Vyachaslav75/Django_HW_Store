from django.core.management.base import BaseCommand

from myapp.models import Product
from random import choice, randint


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        prod = ['Knife', 'Scissors', 'Spoon', 'Fork', 'Tire', 'Glass', 'Earphone', 'Phone']
        for i in range(1, 30):
            product = Product(prod_name=choice(prod) + f'{i}', description='shark', price=randint(10, 200),
                              prod_count=randint(1, 200))
            product.save()
            self.stdout.write(f'{product}')
