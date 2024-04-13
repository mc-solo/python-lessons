class BankAccount:
    def __init__(self, initialBalance, accName):
        self.balance = initialBalance
        self.name = accName

    def get_balance(self):
        print(f"\n{self.name} has ${self.balance:.2f} in the bank account")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposit completed. Account {self.name} has ${self.balance:.2f}")
