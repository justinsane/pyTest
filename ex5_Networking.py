'''
Exercise 5: (Advanced) Change the socket program so that it only shows 
data after the headers and a blank line have been received. Remember 
that recv receives characters (newlines and all), not lines.
'''

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

content = b""

while True:
    data = mysock.recv(512)
    if len(data) < 1: break
    content = content + data

mysock.close()


# Look for the end of the header (2 CRLF)
pos = content.find(b"\r\n\r\n")
print('Header length', pos)
print(content[pos:].decode())

# Code: http://www.py4e.com/code3/socket1.py