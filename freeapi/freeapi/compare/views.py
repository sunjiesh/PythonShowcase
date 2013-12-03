#coding=utf-8

from django.http import HttpResponse
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt

import compare

def index(request):
    """
        测试首页
    """
    t = loader.get_template('compare/index.html')
    c = Context({
        'app': 'My app',
        'message': 'I am the second view.'
    })
    return HttpResponse(t.render(c))

@csrf_exempt
def param(request):
    """
        参数对比页面
    """
    if request.method == 'GET':
        t = loader.get_template('compare/param.html')
        c = Context({
            'app': 'My app',
            'message': 'I am the second view.'
        })
        return HttpResponse(t.render(c))
    else:
        try:
            
            #read params        
            paramTxt1=request.REQUEST["paramTxt1"]
            paramTxt2=request.REQUEST["paramTxt2"]
            paramType=request.REQUEST["paramType"]
            
            
            if(paramType=='1'):
                print 'paramTxt1='+paramTxt1
                print 'paramTxt2='+paramTxt2
                print u'参数类型是普通表单形式参数'
                equalParams,notEqualParams,needlessParams,lostParams,paramArrArr1,paramArrArr2=compare.fromParamsCompare(paramTxt1,paramTxt2)
                
                
                t = loader.get_template('compare/param.html')
                c = Context({
                    'paramTxt1': paramTxt1,
                    'paramTxt2': paramTxt2,
                    'equalParams':formatResult(equalParams,paramArrArr1),
                    'notEqualParams':formatResult(notEqualParams,paramArrArr1),
                    'needlessParams':formatResult(needlessParams,paramArrArr2),
                    'lostParams':formatResult(lostParams,paramArrArr1)
                })
                return HttpResponse(t.render(c))
            else:
                print u'参数类型是Multipart表单形式'
                equalParams,notEqualParams,needlessParams,lostParams,paramArrArr1,paramArrArr2=compare.multipartParamsCompare(paramTxt1,paramTxt2)
                
                
                t = loader.get_template('compare/param.html')
                c = Context({
                    'paramTxt1': paramTxt1,
                    'paramTxt2': paramTxt2,
                    'equalParams':formatResult(equalParams,paramArrArr1,paramType),
                    'notEqualParams':formatResult(notEqualParams,paramArrArr1,paramType),
                    'needlessParams':formatResult(needlessParams,paramArrArr2,paramType),
                    'lostParams':formatResult(lostParams,paramArrArr1,paramType)
                })
                return HttpResponse(t.render(c))                
                
        except ValueError as e:
            print e
        except:
            print u'服务器报错'

def formatResult(paramKeys,paramArr,paramType='1'):
    if paramType=='1':
        paramStr=''
        for paramKey in paramKeys:
            for paramValue in paramArr[paramKey]:
                paramStr=paramStr+paramKey+'='+paramValue+"\n"
        return paramStr
    else:
        paramStr=''
        for paramKey in paramKeys:
            paramStr=paramStr+paramKey+'='+paramArr[paramKey]+"\n"
        return paramStr