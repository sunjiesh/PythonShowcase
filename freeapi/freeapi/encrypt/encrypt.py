#coding=utf-8

import hashlib


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
