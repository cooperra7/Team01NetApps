#!/usr/bin/env python

import wolframalpha
import socket

# Variables for server
host = 'localhost'
port = 5000
backlog = 5
size = 1024

# Wolfram Alpha set up
app_id = "2AYVQ4-869A86X3LQ"
wolfclient = wolframalpha.Client(app_id)

# Have server listen to clients
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)

# Infinite loop
while 1:
    client, address = s.accept()
    data = client.recv(size)

    # Every time server gets input, send that input to Wolfram Alpha
    input = data.decode()
    print(input)
    res = wolfclient.query(input)
    answer = next(res.results).text
    bytes = str.encode(answer)
    print(answer)

    if bytes:
        client.send(answer.encode())
    client.close()
