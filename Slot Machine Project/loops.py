print("Sending a message ...")
# use loops to create a repetation


# the range() function

for i in range(2, 6):
    print(i)
print("################################")

# specifying a starting point, and step size
for i in range(5, 25, 5):
    print(i)

print("################################")
# using a negative step size to count down

for i in range(25, 0, -5):
    print(i)

# generating a list from the range function

numbers = list(range(2, 10))
print(numbers)
