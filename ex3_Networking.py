'''
Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) displaying up to 3000 characters, 
and (3) counting the overall number of characters in the document. Don’t worry about the headers for this exercise, simply show the first 
3000 characters of the document contents.
'''

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/mbox-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

char_count = 0

while True:
    data = mysock.recv(1)
    if len(data) < 1:
        break
    for char in data.strip():
        char_count += 1
    if char_count <= 2999:
        print(data.decode(), end='')
    else:
        break
print()
print('Total Character Count is: ', char_count)

mysock.close()

# Code: http://www.py4e.com/code3/socket1.py