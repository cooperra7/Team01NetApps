#!/usr/bin/python3

import hashlib
import sys
import re

def getmd5(message):
    m = hashlib.md5()
    m.update(message.encode('utf-8'))
    return m.hexdigest()

def makemessage(message):
    return (message, getmd5(message))

# Regex matchs an IPv4 address
#pat = re.compile('^[0-9]?[0-9]?[0-9]\.[0-9]?[0-9]?[0-9]\.[0-9]?[0-9]?[0-9]\.[0-9]?[0-9]?[0-9]$')

# Regex matches strings in example from email
pat = re.compile ('.*?@tomswift ECE4564-Team01.*?')

if pat.match(sys.argv[1]):
    q = makemessage(sys.argv[1])
    print ("{}".format(q))
    print ("message: {}".format(q[0]))
    print ("md5hash: {}".format(q[1]))
else:
    print ("No match for: {}".format(sys.argv[1]))
