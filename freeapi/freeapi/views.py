#coding=utf-8

from django.http import HttpResponse
from django.template import loader, Context


def index(request):
    """
        测试首页
    """
    #return HttpResponse("Hello, world. You're at the poll index.")
    t = loader.get_template('index.html')
    c = Context({
        'app': 'My app',
        'message': 'I am the second view.'
    })
    return HttpResponse(t.render(c))

def custom_500_view(request):
    """
        错误页面
    """
    #return HttpResponse("Hello, world. You're at the poll index.")
    t = loader.get_template('error/500.html')
    c = Context({
        'app': 'My app',
        'message': 'I am the second view.'
    })
    return HttpResponse(t.render(c))

def custom_404_view(request):
    """
        错误页面
    """
    #return HttpResponse("Hello, world. You're at the poll index.")
    t = loader.get_template('error/404.html')
    c = Context({
        'app': 'My app',
        'message': 'I am the second view.'
    })
    return HttpResponse(t.render(c))
    
def custom_403view(request):
    """
        错误页面
    """
    #return HttpResponse("Hello, world. You're at the poll index.")
    t = loader.get_template('error/403.html')
    c = Context({
        'app': 'My app',
        'message': 'I am the second view.'
    })
    return HttpResponse(t.render(c))
    
def custom_400_view(request):
    """
        错误页面
    """
    #return HttpResponse("Hello, world. You're at the poll index.")
    t = loader.get_template('error/400.html')
    c = Context({
        'app': 'My app',
        'message': 'I am the second view.'
    })
    return HttpResponse(t.render(c))
