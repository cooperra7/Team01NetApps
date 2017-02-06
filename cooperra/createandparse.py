#!/usr/bin/python3

import hashlib
import sys

def getmd5(message):
    m = hashlib.md5()
    m.update(message.encode('utf-8'))
    return m.hexdigest()

def makemessage(message):
    return (message, getmd5(message))

q = makemessage(sys.argv[1])
print ("{}".format(q))
print ("message: {}".format(q[0]))
print ("md5hash: {}".format(q[1]))
