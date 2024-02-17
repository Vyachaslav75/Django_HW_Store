from django.shortcuts import render
from django.http import HttpResponse
import logging

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


# Create your views here.
