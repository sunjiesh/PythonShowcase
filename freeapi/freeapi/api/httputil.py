# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:41:08 2013

@author: tom
"""

import urllib2

def downloadFile(path):
    file_name = path.split('/')[-1]
    u = urllib2.urlopen(path)
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)
    file_size_dl = 0
    block_sz = 20480
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)        
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8) * (len(status) + 1)
        print status,
        yield buffer