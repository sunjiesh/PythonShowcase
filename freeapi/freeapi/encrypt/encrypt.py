#coding=utf-8

import hashlib


def genmd5(str):
    """
        GEN MD5 HEX
    """
    if str!='':
        m = hashlib.md5()
        m = m.update(str)
        return m.hexdigest()
    else:
        return ""
