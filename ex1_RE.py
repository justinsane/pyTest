# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. 
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author

# $ python grep.py
# Enter a regular expression: ^X-
# mbox.txt had 14368 lines that matched ^X-

# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4175 lines that matched java$ 4th test!!!

import re
fhand = open('mbox.txt')
user_re = input("Enter a regular expression:  ")
count_list = list()
count = 0

for line in fhand:
    line = line.rstrip()
    x = re.findall(user_re, line)
    if len(x) > 0: 
        count_list.append(x)
        count += 1
print(fhand.name, 'had ', count, 'lines that matched ', user_re,'.', sep='')
