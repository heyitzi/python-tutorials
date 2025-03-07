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