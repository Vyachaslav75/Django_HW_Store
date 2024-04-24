from django.core.management.base import BaseCommand

from myapp.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        for i in range(1, 20):
            user = User(name=f'John{i}', email=f'john{i}@example.com', phone=f'2{i}43{i}34534',
                        address=f'Aasdsf{i}, wewer{i}')
            user.save()
            self.stdout.write(f'{user}')
