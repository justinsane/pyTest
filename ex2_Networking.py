'''
Exercise 2: Change your socket program so that it counts the number of characters it has received and 
stops displaying any text after it has shown 3000 characters. The program should retrieve the entire 
document and count the total number of characters and display the count of the number of characters at 
the end of the document.
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