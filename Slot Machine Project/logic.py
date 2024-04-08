MAX_LINES = 3  # global const for the max number of lines
MAX_BET = 10
MIN_BET = 2


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
                print("Enter a valid num between 1 and 3")
        else:
            print("Input is not a number")
    return lines


# get the number of bets
def get_bet():
    while True:
        bet = input("What would you like to bet?")
        if bet.isdigit:
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Value must be between min and max bet ")
        else:
            print("Please, enter a valid number of bets")
    return bet


# Program should start from the main function
# def main():
#     balance = deposit()
#     lines = get_number_of_lines()
#     bet = get_bet()
#     print(balance, lines)


# main()
get_number_of_lines()
