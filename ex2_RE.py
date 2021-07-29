# Exercise 2: Write a program to look for lines of the form:

# New Revision: 39772

import re
new_list = list()

fhand = open('mbox.txt')
for line in fhand:
    line = line.strip()
    x = re.findall('(New Revision: \d+)', line)
    if len(x) > 0:
        new_list.append(x)
print(new_list[0])