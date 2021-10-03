"""
9. DataStructures :
------------------
A.Numbers :
-----------
B. String :
----------
    1. Write a Python program to calculate the length of a string. "kjgffvjkjf"
    2. Write a Python program to count the number of characters (character frequency) in a string.
            Sample String : google.com'
            Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
    3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
    If the string length is less than 2, return instead of the empty string.
            Sample String : 'w3gfdgfdgfsdgfgfdgfdgource' 'a'
            Expected Result : 'w3ce'
            Sample String : 'w3'
            Expected Result : 'w3w3'
            Sample String : ' w'
            Expected Result : Empty String
    4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
            Sample String : 'restart'
            Expected Result : 'resta$t'
    5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
            Sample String : 'abc', 'xyz'
            Expected Result : 'xyc abz'
    6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
    If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
            Sample String : 'abc'
            Expected Result : 'abcing'
            Sample String : 'string'
            Expected Result : 'stringly'
    7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor',
    replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
            Sample String : 'The lyrics is not that poor!'
                            'The lyrics is poor!'
            Expected Result : 'The lyrics is good!'
                              'The lyrics is poor!'
    8. Write a Python function that takes a list of words and returns the length of the longest one.
    9. Write a Python program to remove the nth index character from a nonempty string.
10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
11. Write a Python program to remove the characters which have odd index values of a given string.
12. Write a Python program to count the occurrences of each word in a given sentence.
13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
        Sample Words : red, white, black, red, green, black
        Expected Result : black, green, red, white,red
15. Write a Python function to create the HTML string with tags around the word(s).
        Sample function and result :
        add_tags('i', 'Python') -> '<i>Python</i>'
        add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
16. Write a Python function to insert a string in the middle of a string.
        Sample function insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
        result :    	insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
        Sample function  : insert_end('Python') -> onononon
        result : insert_end('Exercises') -> eseseses
18. Write a Python function to get a string made of its first three characters of a specified string. If the length of
    the string is less than 3 then return the original string.
        Sample function  : first_three('ipy') -> ipy
        result :  first_three('python') -> pyt
19. Write a Python program to get the last part of a string before a specified character.
        https://www.w3resource.com/python-exercises
        https://www.w3resource.com/python
20. Write a Python function to reverses a string if it's length is a multiple of 4.
21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in
     the first 4 characters.
22.Write a Python program to sort a string lexicographically.
23. Write a Python program to remove a newline in Python.
24. Write a Python program to check whether a string starts with specified characters.
25. Write a Python program to create a Caesar encryption. Note : In cryptography, a Caesar cipher, also known as
 Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known
 encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a
 letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced
 by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
 26. Write a Python program to display formatted text (width=50) as output.
27. Write a Python program to remove existing indentation from all of the lines in a given text.
28. Write a Python program to add a prefix text to all of the lines in a string.
29. Write a Python program to set the indentation of the first line.
30. Write a Python program to print the following floating numbers upto 2 decimal places.
31. Write a Python program to print the following floating numbers upto 2 decimal places with a sign.
32. Write a Python program to print the following floating numbers with no decimal places.
33. Write a Python program to print the following integers with zeros on the left of specified width.
34. Write a Python program to print the following integers with '*' on the right of specified width.
35. Write a Python program to display a number with a comma separator.
36. Write a Python program to format a number with a percentage.
37. Write a Python program to display a number in left, right and center aligned of width 10.
38. Write a Python program to count occurrences of a substring in a string.
39. Write a Python program to reverse a string.
40. Write a Python program to reverse words in a string.
41. Write a Python program to strip a set of characters from a string.
42. Write a Python program to count repeated characters in a string.
        Sample String: 'thequickbrownfoxjumpsoverthelazydog'
        Expected output :
                        o 4
                        e 3
                        u 2
                        h 2
                        r 2
                        t 2
43. Write a Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder.
        Sample output: 	The area of the rectangle is 1256.66cm2
                        The volume of the cylinder is 1254.725cm3
44. Write a Python program to print the index of the character in a string.
        Sample String: w3resource
            Expected output:
                    Current character w position at 0
                    Current character 3 position at 1
                    Current character r position at 2
                    - - - - - - - - - - - - - - - - - - - - - - - - -
                    Current character c position at 8
                    Current character e position at 9
45. Write a Python program to check if a string contains all letters of the alphabet.
46. Write a Python program to convert a string in a list.
47. Write a Python program to lowercase first n characters in a string.
48. Write a Python program to swap comma and dot in a string.
        Sample String: "32.054,23"
        Expected Output: "32,054.23"
49. Write a Python program to count and display the vowels of a given text.
50. Write a Python program to split a string on the last occurrence of the delimiter.
51. Write a Python program to find the first non-repeating character in given string.
52. Write a Python program to print all permutations with given repetition number of characters of a given string.
53. Write a Python program to find the first repeated character in a given string.
54. Write a Python program to find the first repeated character of a given string where the index of first occurrence is smallest.
55. Write a Python program to find the first repeated word in a given string.
56. Write a Python program to find the second most repeated word in a given string.
57.Write a Python program to remove spaces from a given string.
58. Write a Python program to move spaces to the front of a given string.
59. Write a Python program to find the maximum occurring character in a given string.
60. Write a Python program to capitalize first and last letters of each word of a given string.
61. Write a Python program to remove duplicate characters of a given string.
62. Write a Python program to compute sum of digits of a given string.
63. Write a Python program to remove leading zeros from an IP address.
64. Reverse a given string  Input : "Python"   Output : "nohtyP"
65. Reverse each word in given string Input : "I am learing Python Programming Language"   Output : "Language Programming Python learning am I"
66. Reverse each word and reverse word again. Input : "I am learing Python Programming Language"   Output : "agaugnaL gnimmargorP nohtyP gninrael ma I"
67. Write a Python program that accepts a string and calculate the number of digits and letters
        Input : "Python 3.2.5"
        Output : Letters = 6
                 Digits = 3

C. List:
-----------
1. Write a Python program to sum all the items in a list.
2. Write a Python program to multiplies all the items in a list.
3. Write a Python program to get the largest number from a list.
4. Write a Python program to get the smallest number from a list.
5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
        Sample List : ['abc', 'xyz', 'aba', '1221']
                Expected Result : 2
6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
        Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
                Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
7. Write a Python program to remove duplicates from a list.
8. Write a Python program to check a list is empty or not.
9. Write a Python program to clone or copy a list.
10. Write a Python program to find the list of words that are longer than n from a given list of words.
11. Write a Python function that takes two lists and returns True if they have at least one common member.
12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
        Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        Expected Output : ['Green', 'White', 'Black']
13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
15. Write a Python program to shuffle and print a specified list.
16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).
18. Write a Python program to generate all permutations of a list in Python.
19. Write a Python program to get the difference between the two lists.
20. Write a Python program access the index of a list.
21. Write a Python program to convert a list of characters into a string.
22. Write a Python program to find the index of an item in a specified list.
23. Write a Python program to flatten a shallow list.
24. Write a Python program to append a list to the second list.
25. Write a Python program to select an item randomly from a list.
26. Write a python program to check whether two lists are circularly identical.
27. Write a Python program to find the second smallest number in a list.
28. Write a Python program to find the second largest number in a list.
29. Write a Python program to get unique values from a list.
30. Write a Python program to get the frequency of the elements in a list.
31. Write a Python program to count the number of elements in a list within a specified range.
32. Write a Python program to check whether a list contains a sublist.
33. Write a Python program to generate all sublists of a list.
34. Write a Python program to print all the elements in list in ascending order
35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
        Sample list : ['p', 'q']
        n =5
        Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
36. Write a Python program to get variable unique identification number or string.
37. Write a Python program to find common items from two lists.
38. Write a Python program to change the position of every n-th value with the (n+1)th in a list.
        Sample list: [0,1,2,3,4,5]
        Expected Output: [1, 0, 3, 2, 5, 4]
39. Write a Python program to convert a list of multiple integers into a single integer.
        Sample list: [11, 33, 50]
        Expected Output: 113350
40. Write a Python program to split a list based on first character of word.
41. Write a Python program to create multiple lists.
42. Write a Python program to find missing and additional values in two lists.
        Sample data : Missing values in second list: b,a,c
        Additional values in second list: g,h
43. Write a Python program to split a list into different variables.
44. Write a Python program to generate groups of five consecutive numbers in a list.
45. Write a Python program to convert a pair of values into a sorted unique array.
46. Write a Python program to select the odd items of a list.
47. Write a Python program to insert an element before each element of a list.
48. Write a Python program to print a nested lists (each list on a new line) using the print() function.
49. Write a Python program to convert list to list of dictionaries.
        Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
        Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
50. Write a Python program to sort a list of nested dictionaries.
51. Write a Python program to split a list every Nth element.
        Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
        Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
52. Write a Python program to compute the similarity between two lists.
        Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
        Expected Output:
        Color1-Color2: ['white', 'orange', 'red']
        Color2-Color1: ['black', 'yellow']
53. Write a Python program to create a list with infinite elements.
54. Write a Python program to concatenate elements of a list.
55. Write a Python program to remove key values pairs from a list of dictionaries.
56. Write a Python program to convert a string to a list.
57. Write a Python program to check if all items of a list is equal to a given string.
58. Write a Python program to replace the last element in a list with another list.
        Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
        Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
59. Write a Python program to check if the n-th element exists in a given list.
60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
61. Write a Python program to create a list of empty dictionaries.
62. Write a Python program to print a list of space-separated elements.
63. Write a Python program to insert a given string at the beginning of all items in a list.
        Sample list : [1,2,3,4], string : emp
        Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
64. Write a Python program to iterate over two lists simultaneously.
65. Write a Python program to access dictionary keys element by index.
66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
        Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
        Expected Output: [10, 11, 12]
67. Write a Python program to find all the values in a list are greater than a specified number.
68. Write a Python program to extend a list without append.
        Sample data: [10, 20, 30]
                     [40, 50, 60]
        Expected output : [40, 50, 60, 10, 20, 30]
69. Write a Python program to remove duplicates from a list of lists.
        Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        New List : [[10, 20], [30, 56, 25], [33], [40]]
70. Write a Python program to get the depth of a dictionary.
71. Write a Python program to check if all dictionaries in a list are empty or not.
        Sample list : [{},{},{}]
        Return value : True
        Sample list : [{1,2},{},{}]
        Return value : False
72. Generates a two-dimensional array
        Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional
        array. The element value in the i-th row and j-th column of the array should be i*j.
        Note :
        i = 0,1.., m-1
        j = 0,1, n-1.
        Output :
        Input number of rows: 3
        Input number of columns: 4
        [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
73. A list contains group of strings.Convert each word to capital letter and print.
    Input : ["Python","Programming","Language"]
    Output: ["PYTHON","PROGRAMMING","LANGUAGE"]
74. Reverse list of elements and print in upper case
    Input : ["Python","Programming","Language","course"]
    Output: ["COURSE", "LANGUAGE","PROGRAMMING","PYTHON"]
75. Write a Python program to convert month name to a number of days.
        Input : months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
        "October", "November", "December"]
        Output : January : 31
                 February: 28
                 March : 31
                 ....

D. Tuple:
----------
1. Write a Python program to create a tuple.
2. Write a Python program to create a tuple with different data types.
3. Write a Python program to create a tuple with numbers and print one item.
4. Write a Python program to unpack a tuple in several variables.
5. Write a Python program to add an item in a tuple.
6. Write a Python program to convert a tuple to a string.
7. Write a Python program to get the 4th element and 4th element from last of a tuple.
8. Write a Python program to create the colon of a tuple.
9. Write a Python program to find the repeated items of a tuple.
10. Write a Python program to check whether an element exists within a tuple.
11. Write a Python program to convert a list to a tuple.
12. Write a Python program to remove an item from a tuple.
13. Write a Python program to slice a tuple.
14. Write a Python program to find the index of an item of a tuple.
15. Write a Python program to find the length of a tuple.
16. Write a Python program to convert a tuple to a dictionary.
17. Write a Python program to unzip a list of tuples into individual lists.
18. Write a Python program to reverse a tuple.
19. Write a Python program to convert a list of tuples into a dictionary.
20. Write a Python program to print a tuple with string formatting.
        Sample tuple : (100, 200, 300)
        Output : This is a tuple (100, 200, 300)
21. Write a Python program to replace last value of tuples in a list.
        Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
        Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
22. Write a Python program to remove an empty tuple(s) from a list of tuples.
        Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
        Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
23. Write a Python program to sort a tuple by its float element.
        Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
        Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
24. Write a Python program to count the elements in a list until an element is a tuple.


E.Dictionary :
--------------
1. Write a Python program that prints each item and its corresponding type from the following list.
        Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
        Exp Ouput  : 1452 is integer type
                     11.23 is float type
                     .....
2. Write a Python script to sort (ascending and descending) a dictionary by value.
3. Write a Python script to add a key to a dictionary
4. Write a Python script to check if a given key already exists in a dictionary.
5. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the
form (x, x*x)
    Sample Dictionary ( n = 5)
    Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
6. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the
values are square of keys.
   Sample Dictionary
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
7. Write a Python script to merge two Python dictionaries
8. Write a Python program to sum all the items in a dictionary
9. Write a Python program to multiply all the items in a dictionary
10.Write a Python program to map two lists into a dictionary
11.Write a Python program to sort a dictionary by key
12.Write a Python program to get the maximum and minimum value in a dictionary.
13.Write a Python program to remove duplicates from Dictionary
14.19. Write a Python program to combine two dictionary adding values for common keys.
    d1 = {'a': 100, 'b': 200, 'c':300}
    d2 = {'a': 300, 'b': 200, 'd':400}
    Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
15. Write a Python program to print all unique values in a dictionary.
    Sample Data : 	[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},
    {"VIII":"S007"}]
    Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
16. Write a Python program to create and display all combinations of letters, selecting each letter from a different
 key in a dictionary.
        Sample data : {'1':['a','b'], '2':['c','d']}
        Expected Output:
        ac
        ad
        bc
        bd
17. Write a Python program to find the highest 3 values in a dictionary.
18. Write a Python program to combine values in python list of dictionaries.
        Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
        Expected Output: Counter({'item1': 1150, 'item2': 300})
19. Write a Python program to create a dictionary from a string.
        Note: Track the count of the letters from the string.
                Sample String : 'w3resource'
        Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
25. Write a Python program to print a dictionary in table format.
26. Write a Python program to count the values associated with key in a dictionary.
        Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'},
        {'id': 2, 'success': False, 'name': 'Rabi'},
                        {'id': 3, 'success': True, 'name': 'Alex'}
                        ]
                Expected Result: Count of how many dictionaries have success as True
27. Write a Python program to convert a list into a nested dictionary of keys.
28. Write a Python program to sort a list alphabetically in a dictionary.
29. Write a Python program to remove spaces from dictionary keys.
30. Write a Python program to get the top three items in a shop.
        Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
        Expected Output:
        item4 55
        item1 45.5
        item3 41.3
31. Write a Python program to get the key, value and item in a dictionary.
32. Write a Python program to print a dictionary line by line.
33. Write a Python program to check multiple keys exists in a dictionary.
34. Write a Python program to count number of items in a dictionary value that is a list.
35. Write a Python program to sort Counter by value.
        Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
        Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
36. Write a Python program to create a dictionary from two lists without losing duplicate values.
        Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
        Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}})
37. Write a Python program to replace dictionary values with their sum.
38. Write a Python program to match key values in two dictionaries.
        Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
        Expected output: key1: 1 is present in both x and y
F.Set:
----------
1. Write a Python program to create a set.
2. Write a Python program to iteration over sets.
3. Write a Python program to add member(s) in a set.
4. Write a Python program to remove item(s) from set
5. Write a Python program to remove an item from a set if it is present in the set.
6. Write a Python program to create an intersection of sets.
7. Write a Python program to create a union of sets.
8. Write a Python program to create set difference.
9. Write a Python program to create a symmetric difference.
10. Write a Python program to issubset and issuperset.
11. Write a Python program to create a shallow copy of sets.
    Note : Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values
     in the original object.
12. Write a Python program to clear a set.
13. Write a Python program to use of frozensets.
14. Write a Python program to find maximum and the minimum value in a set.
15. Write a Python program to find the length of a set.

G. Arrays:
-----------
1. Write a Python program to create an array of 5 integers and display the array items. Access individual element
through indexes.
2. Write a Python program to append a new item to the end of the array.
3. Write a Python program to reverse the order of the items in the array.
4. Write a Python program to get the length in bytes of one array item in the internal representation.
5. Write a Python program to get the current memory address and the length in elements of the buffer used to hold an
 array?s contents and also find the size of the memory buffer in bytes.
6. Write a Python program to get the number of occurrences of a specified element in an array.
7. Write a Python program to append items from inerrable to the end of the array.
8. Write a Python program to convert an array to an array of machine values and return the bytes representation.
9. Write a Python program to append items from a specified list.
10.Write a Python program to insert a new item before the second element in an existing array.
11.Write a Python program to remove a specified item using the index from an array.
12.Write a Python program to remove the first occurrence of a specified element from an array.
13.Write a Python program to convert an array to an ordinary list with the same items.
"""
