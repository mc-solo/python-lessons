# import math


# # Sting data types
# # literal assignments

# first = "Wondwosen"
# last = "Asegid"

# # checking the type of  data
# # x = 47

# # using the type function to check the data
# # print(type(x))

# # using isinstance

# d_type = isinstance(first, int)  # returns false cuz iss not of the int type
# print(d_type)

# # using a constructor function to define a var

# goal = str("to become a rich, high value man")
# print(goal)

# # concatenation in python
# print(first + " " + last)

# # In python, casting refers to the process of converting one data type to another.
# num_str = 10
# num_int = int(num_str)

# print(num_int)
# print(isinstance(num_int, int))

# bool_str = "True"
# bool_val = bool(bool_str)

# print(type(bool_val))

# # Escaping special characters
# sentence = "I'm back at work!\tHey!\n\nWhere's this at\\located?"
# # print(sentence)

# # String Methods
# #
# multiline = """
# This is a multiline sentence.

#             I am so lucky to have this in my early ages.
# This is the end of multiline sentence.

# """

# print(multiline)
# print(
#     multiline.title()
# )  # converts to a proper case - capitalizing the 1st letter of each word
# print(multiline.replace("lucky", "thankful"))  # find and replace

# # len() - this checks the length of the string
# print(len(multiline))
# multiline += "              "
# multiline = "               " + multiline
# print(len(multiline))

# # building a new menu

# title = "menu".upper()
# newTitle = title.center(47, "*")
# #
# # print(newTitle)
# # print('coffee'.ljust(25, '.') + '$1'.rjust(4,' ' ))
# # print('Americano'.ljust(25, '.') + '$1.25'.rjust(4,' ' ))
# # print('Iced Latte'.ljust(25, '.') + '$1.5'.rjust(4,' ' ))
# # print('Latte'.ljust(25,'.') + '$1.75'.rjust(4,' '))

# # string index values
# print(first[0])  # the first letter of the string
# print(first[-1])  # the last letter of the string
# print(first[1:])  # starts from the second and goes up to the last letter of the string

# # Some methods return boolean data
# print(first.startswith("W"))
# print(first.endswith("W"))  # This shi* is case-sensitive

# # Boolean data type
# myValue = True
# x = bool(False)
# print(type(x))  # type checkin
# print(isinstance(x, bool))  # returns a bool value after comparison

# # Numeric data types

# # Integer Type
# price = 100
# bestPrice = int(80)  # constructor function

# print(isinstance(bestPrice, int))

# # Float Type
# gpa = 4.887
# y = float(5.3)
# print(isinstance(y, float))

# # Complex type
# compValue = 5 + 7j
# print(type(compValue))
# print(compValue.real)
# print(compValue.imag)

# # Built-in-functions
# print(abs(gpa))  # absolute value
# print(round(gpa, 1))  # rounding
# print(math.pi)  # pi from the math class
# print(math.sqrt(64))


# # Casting a string to a number
# zipcode = "10001"
# zip_value = int(zipcode)
# print(type(zip_value))

# # Error if you attempt to cast incorrect data
# # zip_value = int('Mc_solo')


# The int data type
# These are integers withoput any decimal points
age = 21

# The float data type
# Numbers with decimal points
height = 5.9

# The string data type
# Sequence of characters enclosed within single quotes or double quotes
name = "John"

# The boolean data type
# Represents the truth value 'True' or 'False'
is_adult = True

# List
# Ordered collection of items enclosed within a brackets
numbers = [2, 4, 6]

# Tuples
# ordered collection of items enclosed within parentheses
point = (21, 47)

# Dictionary(dict)
# unordered  collection of key-value pairs enclosed within curly braces
person = {"name": "Alice", "age": 30}

# set
# unordered collection of unique items enclosed within curly braces
person = {
    1,
    3,
    5,
}


# Tupples are immutable
student = ("bro", 21, "male")
count_bro = student.count("bro")
print(count_bro)


# single element tuple
single_element_tuple = (47,)  # the comma is important
print(type(single_element_tuple))

# can contain multiple elements
fruits = ("apple", "bannana")

# can contain different data types
mixed_tuple = (True, "True", 1)

# This's a nested tuple
nested_tuple = ((1, 2), ("a", "b"), ("foo", "bar"))


# Tuple unpacking
# allows to assign the individual elements of a tuple to separate variables in a single statement

coordinates = (2, 4)
x, y = coordinates
print("x coordinate:", x)
print("y coordinate:", y)


# Lists are like arrays but very versatile and flexible.
mixed_lists = [1, "Hello", True, "[1, 2, 3]"]
ml_type = type(mixed_lists)
print(ml_type)


# sets are unordered collection of unique elements in python.
# you can perform various mathematical operation on sets
# like union, intersection or a difference
# sets are mutable
# use the constructor set() or curly braces to define a set


set1 = {1, 2, 3, 4, 5}
print(type(set1))


numbers = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]
uniques = set(numbers)  # a set constructor
print(uniques)


# test for membership in python set

my_set = {"a", "b", "c", 1, 2, 3}

print("Is z in the set? ", "z" in my_set)
length = len(my_set)
print(length)

nums = {10, 20, 30, 40}
letters = {"x", "y", "z"}
names = {"John", "Betty", "Natty"}

nums.add(90)  # adds 90 to nums
print(nums)


letters.remove("z")  # removes 'z' from the letters
print(letters)

# sets support mathematical opetations

joined_set = letters.union(nums)  # performs a union operation
print(joined_set)

# can use the | operator for union

name_nums = nums | names
print(name_nums)

# | - union
# & - intersection
# - - difference( relative complement)
# ^ - symmetric difference
