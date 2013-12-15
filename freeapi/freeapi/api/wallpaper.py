# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 14:48:46 2013

@author: tom
"""

from xml.etree import ElementTree
import urllib2

def bingcn():
    """
        bing页面查询
    """
    try:
        response = urllib2.urlopen('http://cn.bing.com/HPImageArchive.aspx?idx=0&n=1')
        respXml=response.read()
        #print respXml
        root = ElementTree.fromstring(respXml)
        print root
        picUrl = root.find("image/url")
        picUrl = picUrl.text
        picUrl = 'http://cn.bing.com'+picUrl
        return picUrl
    except Exception, e:
        print e
        
