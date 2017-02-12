#!/usr/bin/env python

import wolframalpha
import socket
import sys
import hashlib
import pickle

# Variables for server
host = 'localhost'
port = 5000
backlog = 5
size = 1024

# Wolfram Alpha set up
app_id = "2AYVQ4-869A86X3LQ"
wolfclient = wolframalpha.Client(app_id)

def getmd5 (message):
    m=hashlib.md5()
    m.update(message.encode('utf-8'))
    return m.hexdigest()

def makemessage (message):
    return (message, getmd5(message))

# Have server listen to clients
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)

# Infinite loop
while 1:
    client, address = s.accept()
    sdata = client.recv(size)
    
    data = pickle.loads(sdata)
    if (data[1] != getmd5(data[0])):
        print ("ERROR IN MESSAGE SENDING")

    # Every time server gets input, send that input to Wolfram Alpha
    #input = data.decode()
    print(data)
    print ((data[0]))
    res = wolfclient.query(data[0])
    answer = next(res.results).text
    #bytes = str.encode(answer)
    mesanswer = makemessage(answer)
    print(mesanswer)

#    if mesanswer:
 #       client.send(answer.encode())
    client.close()
