'''
Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, 
(2) displaying up to 100 characters, and (3) counting the overall number of characters in the 
document. Don’t worry about the headers for this exercise, simply show the first 100 characters of 
the document contents.
'''
import requests

html = requests.get('http://data.pr4e.org/romeo.txt')
num_words = int(input('Show how many characters: '))
char_count = 0

for line in html:
    data = len(line.decode().strip())
    char_count += data

print(html.content.decode().strip()[0:num_words])
print('Total number of words: ', char_count)


# for line in html:
#     words = line.decode().strip()
#     for word in words:
#         char_count += 1
# print(html.content.decode().strip()[0:num_words])
# print('Total number of words: ', char_count)

# Code: http://www.py4e.com/code3/socket1.py