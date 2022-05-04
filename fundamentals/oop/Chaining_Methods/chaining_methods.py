class User:

    def __init__(self, name):
        self.name = name
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(f"Name: {self.name}, Balance: ${self.balance}")

    #Bonus: Transfer Money
    def transfer_money(self, amount, account):
        self.balance -= amount
        account.balance += amount
        self.display_user_balance()
        account.display_user_balance()
        return self

sean = User("Sean")
giggles = User("Mr. Giggles")
frankenstein = User("Dr. Frankenstein")

sean.make_deposit(887).make_deposit(737).make_deposit(502).make_withdrawal(1307)

print("After 1st User Transactions:")
sean.display_user_balance()

print("-" * 15)

giggles.make_deposit(496).make_deposit(383).make_withdrawal(208).make_withdrawal(179)

print("After 2nd User Transactions:")
giggles.display_user_balance()

print("-" * 15)

frankenstein.make_deposit(996).make_withdrawal(283).make_withdrawal(108).make_withdrawal(779)

print("After 3rd User Transactions:")
frankenstein.display_user_balance()

print("-" * 15)

print("After Transfer:")
sean.transfer_money(298, frankenstein)

