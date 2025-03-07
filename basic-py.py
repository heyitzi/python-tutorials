# data types
name = "Itz"

# returns boolean
type(name) == str
isinstance(name, str)

# convert str to int
age = int("32")

# boolean operator
condition1 = True
condition2 = False

not condition1 #False
condition1 and condition2 #False
condition1 or condition2 #True

# OR operator in an expression returns the first value that's not falsie, otherwise will return the last one
print(0 or 1) ## 1
print(False or 'hey') ## 'hey'
print ('hi' or 'hey') ## 'hi'
print([] or False) ## 'False' ('[]' is considered falsie value)
print(False or []) ## '[]'

# AND only evaluates the second argument if the first one is True
print(0 or 1) ## 0
print(False or 'hey') ## 'False'
print ('hi' or 'hey') ## 'hey'
print([] or False) ## '[]'
print(False or []) ## 'False'

# Ternary Operator
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False
    
def is_adult2(age):
    return True if age >= 18 else False

# Multiline strings using 3 quotation marks
print("""My name
is Itz
""")

# common string methods (they all return a new modified string, none alter the original string):
# .isalpha() # check string contains only characters & is not empty
# .isalnum() # check string contains character or numbers & is not empty
# .isdecimal() #check string contains digits & is not empty
# .lower() # convert lowercase
# .islower() # check is lowercase
# .upper() # convert uppercase
# .isupper() # check is uppercase
# .title() # convert to capitalized
# .startswith() # check starts with a specific substring
# .endswith() # check ends with a specific substring
# .replace() # replace part of a string
# .split() # split string on a specific character separator
# .strip() # trim the whitespace from string
# .join() # append new letters
# .find() # find the position of a substring

#  escaping characters (adding special characters in a string)
string1 = 'adding \"quotations\" to the string'
print(string1)

string2 = "now I want \na new line"
print(string2)

# Slicing
print(name[1:3]) # starts in index 1 and ends in the previous index (in this case 2)
print(name[:5]) # from the start until before index 5
print(name[3:]) # from 3 until the end of the string

# booleans
done_num = 8 # all numbers are True except 0
if done_num:
    print("yes")
else:
    print("no")

done_str = "" # all strings are True unless empty (same with lists, tuples and dictionaries)
if done_str:
    print("yes")
else:
    print("no")

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read]) # returns True
# any function will return True if one of them is True

ready_to_serve = all([book_1_read, book_2_read]) # returns False
# all functions only returns True if ALL of them are True

# Enums = readable names that are bound to a constant value
from enum import Enum
# State can be anything you want
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(list(State))

# input
age = input("What is your age? ")
print(f"Your age is {age}")

