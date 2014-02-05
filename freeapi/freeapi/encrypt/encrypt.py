#coding=utf-8

import hashlib
import base64
import urllib2


import re

def genmd5(paramStr):
    """
        GEN MD5 HEX
    """
    if paramStr!='':
        print "orign str is "+paramStr
        m = hashlib.md5()
        m.update(paramStr)
        result=m.hexdigest()
        return result;
    else:
        print "no param";
        return ""

def crashmd5(encryptStr):
    """
        decoder str to plaintext
    """
    print encryptStr
    response = urllib2.urlopen('http://www.md5-hash.com/md5-hashing-decrypt/'+encryptStr)
    html=response.read()
    result=""    
    compileResult = re.findall(r'<strong class="result">(.*)</strong>', html)
    if len(compileResult)>0:
        for resultItem in compileResult:
            result=result+resultItem+"\n"
    else:
        result=u"没有找到符合条件的字符串"
    print result
    return result
    
def encodeBase64(plainText):
    """
        encrypt base64 str
    """
    if plainText!='':
        encoded = base64.b64encode(plainText)
        return encoded
    else:
        return ""
        
def decodeBase64(encryptStr):
    if encryptStr!='':
        data = base64.b64decode(encryptStr)
        return data
    else:
        return ""
        
def encryptThunder(plainText):
    """
        迅雷地址加密
    """
    if plainText!='':
        plainText="AA"+plainText+"ZZ"
        print plainText
        plainText=unicode(plainText,"utf-8")
        plainText=plainText.encode("gbk")
        encoded = base64.b64encode(plainText)
        encoded="thunder://"+encoded
        return encoded
    else:
        return ""

def decryptThunder(encryptStr):
    if encryptStr!='':
        if encryptStr.startswith('thunder://'):#迅雷协议
            encryptStr=encryptStr[encryptStr.rindex("/")+1:]
            print encryptStr
            data = base64.b64decode(encryptStr)
            print data
            try:
                data=unicode(data,"gb2312")
                data=data.encode("utf-8")
            except Exception,e:
                print e
            if data.startswith("AA"):
                data=data[2:]
            if data.endswith("ZZ"):
                data=data[:-2]
            return data
    else:
        return ""