#coding=utf-8

from django.http import HttpResponse
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt

import encrypt

def index(request):
    t = loader.get_template('encrypt/index.html')
    c = Context({
        'app': 'My app',
        'message': 'I am the second view.'
    })
    return HttpResponse(t.render(c))

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

@csrf_exempt      
def crashmd5(request,encryptStr):
    print encryptStr
    if encryptStr!='':
        return HttpResponse(encrypt.crashmd5(encryptStr))
    else:
        return HttpResponse("Please Input String")

@csrf_exempt
def base64(request):
    if request.method == 'GET':
        t = loader.get_template('encrypt/base64.html')
        c = Context({
            'app': 'My app',
            'message': 'I am the second view.'
        })
        return HttpResponse(t.render(c))
    else:

        #请求参数        
        requestStr=request.REQUEST['str']
        encryptType=request.REQUEST['encryptType']
        print requestStr
        print encryptType
        #初始化返回        
        result=''        
        if requestStr != '':
            if encryptType=='encode':
                plainText=requestStr.encode('utf-8')
                print plainText
                result=encrypt.encodeBase64(str(plainText))
            elif encryptType=='decode':
                result=encrypt.decodeBase64(requestStr)
            else:
                pass
        else:
            result=u'没有提交参数'
        return HttpResponse(result)

@csrf_exempt        
def thunder(request):
    if request.method == 'GET':
        t = loader.get_template('encrypt/thunder.html')
        c = Context({
            'app': 'My app',
            'message': 'I am the second view.'
        })
        return HttpResponse(t.render(c))
    else:
        #请求参数        
        requestStr=request.REQUEST['str']
        encryptType=request.REQUEST['encryptType']
        print requestStr
        print encryptType
        #初始化返回        
        result=''        
        if requestStr != '':
            if encryptType=='encode':
                plainText=requestStr.encode('utf-8')
                print plainText
                result=encrypt.encryptThunder(str(plainText))
            elif encryptType=='decode':
                encryptStrArr=requestStr.split("\n")
                for encryptStr in encryptStrArr:
                    print "encryptStr="+encryptStr
                    result=result+"\n"+encrypt.decryptThunder(encryptStr)
            else:
                pass
        else:
            result=u'没有提交参数'
        return HttpResponse(result)