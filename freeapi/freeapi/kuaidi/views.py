#coding=utf-8

import random

import urllib
from django.http import HttpResponse
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt

def index(request):
    """
        测试首页
    """
    #return HttpResponse("Hello, world. You're at the poll index.")
    t = loader.get_template('kuaidi/index.html')
    c = Context({
        'app': 'My app',
        'message': 'I am the second view.'
    })
    return HttpResponse(t.render(c))

@csrf_exempt
def search(request):
    try:
        expressNo=request.REQUEST['no']
        expressCompany=request.REQUEST['company']
        if(expressNo!='' and expressCompany!=''):
            return HttpResponse(searchExpress(expressNo,expressCompany))
        else:
            return HttpResponse(u"请提交内容")
    except Exception, e:
                print e
    return index(request)

def searchExpress(expressNo,company='yto'):
    if company=='yto':
        return searchYto(expressNo)
    elif company=='zto':
        return searchZto(expressNo)
    elif company=='yunda':
        return searchYd(expressNo)
    else:
        return u"暂不支持此公司查询"

def searchYto(expressNo):
    """
        圆通快递查询
    """
    rnd = random.randint(0,1)
    params = urllib.urlencode({'wen': expressNo,'action':'ajax','rnd':rnd})
    f = urllib.urlopen("http://www.kiees.cn/yto.php?%s" % params)
    return f.read().decode('utf8')
    
def searchZto(expressNo):
    """
        中通快递查询
    """
    rnd = random.randint(0,1)
    params = urllib.urlencode({'wen': expressNo,'action':'ajax','rnd':rnd})
    f = urllib.urlopen("http://www.kiees.cn/zto.php?%s" % params)
    return f.read().decode('utf8')

def searchYd(expressNo):
    """
        韵达快递查询
    """
    rnd = random.randint(0,1)
    params = urllib.urlencode({'wen': expressNo,'rnd':rnd,'channel':''})
    f = urllib.urlopen("http://www.kiees.cn/yd.php?%s" % params)
    return f.read().decode('utf8')