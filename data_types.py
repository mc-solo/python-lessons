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
