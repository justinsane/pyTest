# Exercise 2: Write a program to look for lines of the form:

# New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.

# Enter file:mbox.txt
# 38549

# Enter file:mbox-short.txt
# 39756

import re
new_list = list()
count = 0
sum = 0

filename = input("Enter file:  ")
fhand = open(filename)
for line in fhand:
    line = line.strip()
    x = re.findall('New Revision: (\d+)', line)

    if len(x) > 0:
        new_list.append(x)
        count += 1
        for integer in x:
            sum = sum + int(integer)
average = int(sum/count)
print(average)
        
