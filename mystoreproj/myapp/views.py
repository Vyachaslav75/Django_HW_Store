from django.shortcuts import render
from django.http import HttpResponse
import logging
from .models import Order
from .models import User
from .models import Product
from datetime import date, timedelta
from django.core.files.storage import FileSystemStorage
from .forms import ProductForm

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
    my_order = {'user': user, 'prods': prods}
    # return HttpResponse(orders)
    return render(request, 'myapp/get_products.html', my_order)


def upload_image(request):
    if request.method == 'POST':
        # form = ImageForm(request.POST, request.FILES)
        form = ProductForm(request.POST) #, request.FILES)
        if form.is_valid():
            prod_name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            prod_count = form.cleaned_data['prod_count']
            add_date = form.cleaned_data['add_date']
            image = form.cleaned_data['image']
            #fs = FileSystemStorage()
            #fs.save(image.name, image)
            product = Product(prod_name, description, price, prod_count, add_date, image)
            product.save()
        else:
            print('HI')
            form = ProductForm()
            message = 'Заполните форму'
            return render(request, 'myapp/upload_image.html', {'form': form, 'message': message})
