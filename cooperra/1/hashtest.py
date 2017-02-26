#!/usr/bin/python3

import hashlib

def getmd5(message):
    m = hashlib.md5()
    m.update(message.encode('utf-8'))
    print("{}".format(m.hexdigest()))

getmd5("message")
