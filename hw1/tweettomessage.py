#!/usr/bin/python3

import hashlib
import sys
import re
import pickle
import socket

host = 'localhost'
port = 5000
backlog = 5
side = 1024

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
        r = pickle.dumps(q)
        print("{}".format(r))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect ((host, port))
        s.send(r)
        response = s.recv(1024)
        data = pickle.loads(response)
        print (data)
        s.close()
