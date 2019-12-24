"""
Python PIL | Image filter with ImageFilter module:
=================================================
PIL is the Python Imaging Library which provides the python interpreter
 with image editing capabilities.
The ImageFilter module contains definitions for a pre-defined
 set of filters, which can  be used with the Image.filter() method.
"""
# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if alphabet in vowels:
        return True
    else:
        return False


filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)

# importing pandas as pd 

import pandas as pd

# Creating the Series
sr1 = 0
sr = pd.Series([80, 25, 3, 25, 24, 6, sr1])
sr1 = sum(list(sr))
print(sr1)
# Create the Index 
index_ = ['Coca Cola', 'Sprite', 'Coke', 'Fanta', 'Dew', 'ThumbsUp', 'Total  =']
# set the index
sr = pd.Series([80, 25, 3, 25, 24, 6, sr1])
sr.index = index_
# Print the series 
print(sr)
