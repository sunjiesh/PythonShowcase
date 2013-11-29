#coding=utf-8

from django.http import HttpResponse
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt

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
            print 'paramTxt1='+paramTxt1
            print 'paramTxt2='+paramTxt2
            
            #params to arr
            paramArr1=paramTxt1.split("&")
            paramArr2=paramTxt2.split("&")
            print paramArr1
            print paramArr2
            
            #存放到字典中，Value为List
            paramArrArr1={}
            paramArrArr2={}
    
            for tempParam in paramArr1:
                if "=" in tempParam:
                    tempParamArr=tempParam.split("=")
                    tempParamName=''
                    tempParamValue=''
                    if(len(tempParamArr)==1):
                        tempParamName=tempParamArr[0]
                    elif(len(tempParamArr)==2):
                        tempParamName=tempParamArr[0]
                        tempParamValue=tempParamArr[1]
                    else:
                        tempParamName=tempParamArr[0]
                        tempParamValue=tempParam.replace(tempParamName+"=")
                    if paramArrArr1.has_key(tempParamName):
                        paramArrValue=paramArrArr1[tempParamName]
                        paramArrValue=paramArrValue.append(tempParamValue)
                    else:
                        paramArrArr1[tempParamName]=[tempParamValue];
            for tempParam in paramArr2:
                if "=" in tempParam:
                    tempParamArr=tempParam.split("=")
                    tempParamName=''
                    tempParamValue=''
                    if(len(tempParamArr)==1):
                        tempParamName=tempParamArr[0]
                    elif(len(tempParamArr)==2):
                        tempParamName=tempParamArr[0]
                        tempParamValue=tempParamArr[1]
                    else:
                        tempParamName=tempParamArr[0]
                        tempParamValue=tempParam.replace(tempParamName+"=")
                    if paramArrArr2.has_key(tempParamName):
                        paramArrValue=paramArrArr2[tempParamName]
                        paramArrValue=paramArrValue.append(tempParamValue)
                    else:
                        paramArrArr2[tempParamName]=[tempParamValue];
                        
            print paramArrArr1
            print paramArrArr2
            
            
            equalParams=[]
            notEqualParams=[]
            needlessParams=[]
            lostParams=[]
            
            
            #遍历数组，处理判断是否是却少的，以及不一情况
            for paramKey in paramArrArr1:
                if paramKey in paramArrArr2:            
                    paramArrArrValue1=paramArrArr1[paramKey]
                    paramArrArrValue2=paramArrArr2[paramKey]
                    paramArrArrValue1=sorted(paramArrArrValue1)
                    paramArrArrValue2=sorted(paramArrArrValue2)
                    if paramArrArrValue1==paramArrArrValue2:
                        equalParams.append(paramKey)
                    else:
                        notEqualParams.append(paramKey)
                else:
                    lostParams.append(paramKey)
            
            #遍历数组，处理判断是否是多余的参数
            for paramKey in paramArrArr2:
                if paramKey in paramArrArr1:
                    pass
                else:
                    needlessParams.append(paramKey)
            
            print '结果如下'
            print '相等的参数是'
            print equalParams
            print '不想等的参数是'
            print notEqualParams
            print '多余的参数是'
            print needlessParams
            print '缺少的参数是'
            print lostParams
            
            
            
                        
            
            
            t = loader.get_template('compare/param.html')
            c = Context({
                'paramTxt1': paramTxt1,
                'paramTxt2': paramTxt2,
                'equalParams':str(equalParams),
                'notEqualParams':str(notEqualParams),
                'needlessParams':str(needlessParams),
                'lostParams':str(lostParams)
            })
            return HttpResponse(t.render(c))
        except ValueError as e:
            print e
        