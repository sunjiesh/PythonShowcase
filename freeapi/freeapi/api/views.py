#coding=utf-8

import random, string

from django.http import HttpResponse
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt

import wallpaper
import httputil

import uuid

def getWallpaper(request,keywords):
    """
        请求
    """
    download=request.GET.get('download')
    print keywords
    picUrl=''
    if keywords=='bing':
        picUrl=wallpaper.bingcn()
    else:
        print u'暂不支持此关键字查询'
        return HttpResponse(u'暂不支持此关键字查询')
    if picUrl!='':
        if download!=None and download.lower()=='true':
            imageBytes=httputil.downloadFile(picUrl)
            return HttpResponse(imageBytes, mimetype="image/jpeg")
        else:
            return HttpResponse(picUrl)
    else:
        return HttpResponse(u'找不到结果')
        
def downloadPic(request):
    path=request.GET.get('path')
    print path
    if path!='':
        imageBytes=httputil.downloadFile(path)
    return HttpResponse(imageBytes, mimetype="image/jpeg")
        
def genuuid(request):
    """
        gen uuid str
    """
    tempStr=uuid.uuid4()
    print tempStr
    return HttpResponse(tempStr)

@csrf_exempt
def genrandom(request):
    """
        gen uuid str
    """
    tempStr=''
    randomlength=request.POST['len']
    if randomlength=='':
        randomlength=32
    else:
        randomlength=int(randomlength)
    if not request.POST.has_key('cbRule'):
        return HttpResponse("请选择字符串内容")  
    if request.POST['cbRule']:
        chars=""
        resultstr=''
        cbRuleList=request.POST.getlist('cbRule')
       	print cbRuleList
        for cbRule in cbRuleList:
            if cbRule=='0':
                chars=chars+'1234567890'
            elif cbRule=='1':
                chars=chars+'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
        print chars
        for i in range(randomlength):
            resultstr+=chars[random.randint(0, len(chars)-1)]
        print resultstr
        return HttpResponse(resultstr)
    return HttpResponse(tempStr)
