import logging

try:
    numerator = int(input("Enter the numerator\n"))
    denominator = int(input("Enter the divider\n"))
    result = numerator / denominator
    print(result)
except:
    print("Something went wrong")
