#!/usr/bin/python3

import hashlib
import sys
import re
import pickle

if len(sys.argv) != 2:
    print ("Usage: {} <message>".format(sys.argv[0]))
    sys.exit(1)

def getmd5 (message):
    m = hashlib.md5()
    m.update(message.encode('utf-8'))
    return m.hexdigest()

def makemessage (message):
    return (message, getmd5(message))

if re.match('.*?@tomswift ECE4564-Team01.*?', sys.argv[1]):
    fields = sys.argv[1].split('_')
    if re.match('^[12]?[0-9]?[0-9]\.[12]?[0-9]?[0-9]\.[12]?[0-9]?[0-9]\.[12]?[0-9]?[0-9]:[1-6]?[0-9]?[0-9]?[0-9]?[0-9]$', fields[1]):
        q = makemessage(fields[2])
        print ("{}".format(q))
        s = pickle.dumps(q)
        print("{}".format(s))
        t = pickle.loads(s)
        print ("{}".format(t))
