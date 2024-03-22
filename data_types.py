import math


# Sting data types
# literal assignments

first = 'Wondwosen'
last = 'Asegid'

# checking the type of  data
# x = 47

# using the type function to check the data
# print(type(x))

# using isinstance

d_type = isinstance(first, int)  # returns false cuz iss not of the int type
print(d_type)

# using a constructor function to define a var

goal = str('to become a rich, high value man')
print(goal)

# concatenation in python
print(first + ' ' + last)

# In python, casting refers to the process of converting one data type to another.
num_str = 10
num_int = int(num_str)

print(num_int)
print(isinstance(num_int, int))

bool_str = 'True'
bool_val = bool(bool_str)

print(type(bool_val))

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
# print(sentence)

# String Methods
#
multiline = '''
This is a multiline sentence.

            I am so lucky to have this in my early ages.
This is the end of multiline sentence.

'''

print(multiline)
print(multiline.title())  # converts to a proper case - capitalizing the 1st letter of each word
print(multiline.replace('lucky', 'thankful'))  # find and replace

# len() - this checks the length of the string
print(len(multiline))
multiline += '              '
multiline = '               ' + multiline
print(len(multiline))

# building a new menu

title = 'menu'.upper()
newTitle = title.center(47, '*')
#
# print(newTitle)
# print('coffee'.ljust(25, '.') + '$1'.rjust(4,' ' ))
# print('Americano'.ljust(25, '.') + '$1.25'.rjust(4,' ' ))
# print('Iced Latte'.ljust(25, '.') + '$1.5'.rjust(4,' ' ))
# print('Latte'.ljust(25,'.') + '$1.75'.rjust(4,' '))

# string index values
print(first[0])  # the first letter of the string
print(first[-1])  # the last letter of the string
print(first[1:])  # starts from the second and goes up to the last letter of the string

# Some methods return boolean data
print(first.startswith('W'))
print(first.endswith('W'))  # This shi* is case-sensitive

# Boolean data type
myValue = True
x = bool(False)
print(type(x))  # type checkin
print(isinstance(x, bool))  # returns a bool value after comparison

# Numeric data types

# Integer Type
price = 100
bestPrice = int(80)  # constructor function

print(isinstance(bestPrice, int))

# Float Type
gpa = 4.887
y = float(5.3)
print(isinstance(y, float))

# Complex type
compValue = 5 + 7j
print(type(compValue))
print(compValue.real)
print(compValue.imag)

# Built-in-functions
print(abs(gpa))  # absolute value
print(round(gpa, 1))  # rounding
print(math.pi)  # pi from the math class
print(math.sqrt(64))


# Casting a string to a number
zipcode = '10001'
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
# zip_value = int('Mc_solo')

