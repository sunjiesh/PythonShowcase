#coding=utf-8

from django.http import HttpResponse

import wallpaper
import httputil

def getWallpaper(request,keywords):
    """
        请求
    """
    print keywords
    if keywords=='bing':
        picUrl=wallpaper.bingcn()
        return HttpResponse(picUrl)
    else:
        print u'暂不支持此关键字查询'
        return HttpResponse(u'暂不支持此关键字查询')
        
def downloadPic(request):
    path=request.GET.get('path')
    print path
    if path!='':
        imageBytes=httputil.downloadFile(path)
    return HttpResponse(imageBytes, mimetype="image/jpeg")
        

