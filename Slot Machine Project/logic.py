def deposit():
    while True:
        amount = input("what would you like to deposit? $")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Aamount must be greater than 0.")
        else:
            print("Please, enter a number.")
    return amount
