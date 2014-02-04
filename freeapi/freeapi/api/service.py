# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 20:25:58 2014

@author: tom
"""

import random
import urllib
import json
from BeautifulSoup import BeautifulSoup


def getCityFromIp(ip):
    """
        根据IP地址获取城市地址
    """
    result=''
    try:
        rnd = random.randint(0,1)
        params = urllib.urlencode({'ip': ip,'rnd':rnd})
        url="http://ip.cn/index.php?%s" %params
        print url
        response = urllib.urlopen(url)
        respXml=response.read()
        #print respXml
        parser = BeautifulSoup(respXml)
        #print parser
        divResult=parser.findAll('div',attrs={'id':'result'})
        divResult=divResult[0].find('div')
        #print divResult
        divDontents=divResult.contents
        print divDontents
        if len(divDontents)>=2:
            result=divDontents[1]
            result=result.text
            result=result.replace('GeoIP:','')
            if result.__contains__(','):
                result=result.split(',')[0]
            print result
    except Exception, e:
        print e
    return result


    
def getWeatherFromCity(cityName='Shanghai'):
    """
        根据城市获取当前天气，通过调用中国天气网接口查询
    """
    #初始化城市代码列表
    cityCode={}
    cityCode['shanghai']='101020100'#上海
    cityCode['beijing']='101010100'#北京
    cityCode['tianjin']='101030100'#天津
    cityCode['chongqing']='101040100'#重庆
    
    cityName=cityName.lower()
    cityName=cityName.replace(' ','')
    resultStr=''
    print 'cityName='+cityName
    try:
        if cityCode.has_key(cityName):
            weatherUrl='http://m.weather.com.cn/data/'+cityCode[cityName]+'.html'
            print weatherUrl
            response = urllib.urlopen(weatherUrl).read()
            print response
            def as_complex(dct):
                if 'weatherinfo' in dct:
                    return as_complex(dct['weatherinfo'])
                return dct
            resultJson=json.loads(response,encoding='UTF-8',object_hook=as_complex)
            city=resultJson['city']
            temp1=resultJson['temp1']
            weather1=resultJson['weather1']
            wind1=resultJson['wind1']
            resultStr=unicode(city)+u'：'+temp1+','+weather1+','+unicode(wind1)
            print resultStr
        else:
            resultStr='不支持城市查询'
    except Exception,e:
        print e
    return resultStr
        

    