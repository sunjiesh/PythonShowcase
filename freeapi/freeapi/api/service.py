# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 20:25:58 2014

@author: tom
"""

import random
import urllib
from BeautifulSoup import BeautifulSoup


def getCityFromIp(ip):
    """
        根据IP地址获取城市地址
    """
    result=''
    try:
        rnd = random.randint(0,1)
        params = {'ip': ip,'rnd':rnd}
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