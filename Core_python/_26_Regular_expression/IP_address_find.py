# Extract IP address from file using Python

# Algorithm:
#
# Import the re module for regular expression.
# Open the file using the open() function.
# Read all the lines in the file and store them in a list. Declare
# the pattern for IP addresses.The regex pattern is:
#
# r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'


# importing the module
import re

# opening and reading the file
with open('C:/Users/user/Desktop/New Text Document.txt') as fh:
    fstring = fh.readlines()

    # declaring the regex pattern for IP addresses
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    # pattern = re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)
    # {3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')
    lst = []
    for line in fstring:
        lst.append(pattern.search(line)[0])
    print(lst)

# The above Python program displays any kind of IP addresses present in the file. We can also display the valid IP
# addresses.
#
# Rules for a valid IP Address :
#
# The numbers should be in a range of 0-255
# It should consist of 4 cells separated by ‘.’

# Explanation of Regular Expression used for valid IP:
#
# Since we cannot use 0-255 range in regular expression we divide the same in 3 groups:
#
# 25[0-5] – represents numbers from 250 to 255
# 2[0-4][0-9] – represents numbers from 200 to 249
# [01]?[0-9][0-9]?- represents numbers from 0 to 199

