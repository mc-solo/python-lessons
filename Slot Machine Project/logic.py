MAX_LINES = 3  # global const for the max number of lines


# Get amount from the user
def deposit():
    while True:
        amount = input("what would you like to deposit? $")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please, enter a number.")
    return amount


# get the number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")  "
        )
        if lines.isdigit:
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
        else:
            print("Please, enter a numbert")
    return lines


# Program should start from the main function
def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)


main()
