from django.shortcuts import render
from django.http import HttpResponse
import logging
from .models import Order
from .models import User
# from models import Product
from datetime import date, timedelta

logger = logging.getLogger(__name__)


def index(request):
    html = '''
        <title>Первая страница</title>
        <h1>Первая страница магазина</h1>
        <p>Привет!!! </p>
        '''
    logger.info('Main page accessed')
    return HttpResponse(html)


def mybase(request):
    html = '''
            <title>Base page</title>
            <h1>Base page</h1>
            '''
    logger.info('Base page accessed')
    return HttpResponse(html)


def get_products(request, id, days):
    get_date = date.today() - timedelta(days=days)
    user = User.objects.filter(pk=id).first()

    orders = Order.objects.filter(customer=user, date_ordered__gt=get_date).all()
    prods = set()
    for order in orders:
        for prod in order.products.all():
            prods.add(prod.name())
    my_order={'user': user, 'prods': prods}
    #return HttpResponse(orders)
    return render(request,'myapp/get_products.html', my_order)
