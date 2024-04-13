import logging

try:
    numerator = int(input("Enter the numerator\n"))
    denominator = int(input("Enter the divider\n"))
    result = numerator / denominator
    print(result)

except ZeroDivisionError:
    print("You can't divide by 0, idiot")

except ValueError:
    print("Choose only numbers, you idiot")

except Exception:
    print("Something went wrong")
