'''
Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page. 
You can use split('/') to break the URL into its component parts so you can extract the host name for the socket 
connect call. Add error checking using try and except to handle the condition where the user enters an improperly 
formatted or non-existent URL.
'''

import socket
import re

while True:
    my_web = input('Enter URL:  ')
    check = re.search('https*://*[w.]*\S+.com+', my_web)
    print(check)
    if check == None:
        print("Bad URL - Try again.")
        continue
    else:
        break

re_web = re.findall('https*://*[w.]*(\S+.com)', my_web)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((re_web[0], 80))
cmd = 'GET my_web HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

# Code: http://www.py4e.com/code3/socket1.py