#coding=utf-8

from django.http import HttpResponse
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt

import encrypt

def md5(request):
    t = loader.get_template('encrypt/md5.html')
    c = Context({
        'app': 'My app',
        'message': 'I am the second view.'
    })
    return HttpResponse(t.render(c))

@csrf_exempt
def genmd5(request):
    requestStr=request.REQUEST['str']
    print requestStr
    if requestStr!='':
        return HttpResponse(encrypt.genmd5(requestStr))
    else:
        return HttpResponse("Please Input String")
