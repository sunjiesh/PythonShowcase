#coding=utf-8

from django.http import HttpResponse

import wallpaper
import service
import httputil

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


def getIp(request):
    ipAddress=service.getIp()
    print ipAddress
    return HttpResponse(ipAddress)

