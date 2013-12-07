#coding=utf-8

import hashlib
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
        encrypt str to plaintext
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
    