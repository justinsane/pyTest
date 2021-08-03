'''
Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags 
from the retrieved HTML document and display the count of the paragraphs as the 
output of your program. Do not display the paragraph text, only count them. Test 
your program on several small web pages as well as some larger web pages.
'''

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# while True:
#     url = input('Enter URL:  ')
#     check = re.search('https*://*[w.]*\S+.com+', url)
#     if check == None:
#         print("Bad URL - Try again.")
#         continue
#     else:
#         break

# html = urllib.request.urlopen(url, context=ctx).read()
html = urllib.request.urlopen('https://pythonbooks.org/about/', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

p_count = 0
for tag in soup.find_all('p'):
    p_count += 1

print(p_count)

# Code: http://www.py4e.com/code3/urllinks.py