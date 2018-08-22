# Extracting Data With Regular Expressions: In this assignment you will read through and parse a file with text and
# numbers. You will extract all the numbers in the file and compute the sum of the numbers.

import re

name = input("Enter file:")
if len(name) < 1: name = "regex_sum_127059.txt"
handle = open(name)

total = 0

for line in handle:
    y = re.findall('[0-9]+', line)
    for num in y:
        total = total + int(num)

print(total)
