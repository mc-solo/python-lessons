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

print("################################")

for i in numbers:
    print(i)

print("################################")
count = 0

while count < 5:
    print(count)
    count += 1
print("while loop done")

print("################################")
# break and continue

for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)

# nested loops

for i in range(4):
    for j in range(2):
        print(i, j)
