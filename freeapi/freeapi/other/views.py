#coding=utf-8

from django.http import HttpResponse
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt

def index(request):
    """
        测试首页
    """
    #return HttpResponse("Hello, world. You're at the poll index.")
    t = loader.get_template('random/index.html')
    c = Context({
        'app': 'My app',
        'message': 'I am the second view.'
    })
    return HttpResponse(t.render(c))
