# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 20:25:58 2014

@author: tom
"""

import urllib2


def getIp():
    """
        获取ip地址
    """
    response = urllib2.urlopen('http://ifconfig.me/ip')
    respXml=response.read()
    ipaddress=respXml
    print ipaddress
    return ipaddress