#coding=utf-8

import random

import urllib
from django.http import HttpResponse

def index(request):
    """
        测试首页
    """
    return HttpResponse("Hello, world. You're at the poll index.")

def search(request):
    try:
        expressNo=request.REQUEST['no']
        return HttpResponse(searchExpress(expressNo))
    except Exception, e:
                print e
    return index(request)

def searchExpress(expressNo,company='yto'):
    if company=='yto':
        return searchYto(expressNo)
    else:
        return u"暂不支持公司查询"

def searchYto(expressNo):
    rnd = random.randint(0,1)
    params = urllib.urlencode({'wen': expressNo,'action':'ajax','rnd':rnd})
    f = urllib.urlopen("http://www.kiees.cn/yto.php?%s" % params)
    return f.read().decode('utf8')
