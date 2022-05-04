class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount < 0):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + (.01 * self.int_rate))
        return self

    # Bonus: use a class method to print all instances of Bank Account's info
    @classmethod
    def all_account_info(cls):
        for account in cls.all_accounts:
            print(f"Balance: ${account.balance}")

account1 = BankAccount(3, 4357)
account2 = BankAccount(2, 3862)

account1.deposit(276).deposit(641).deposit(397).withdraw(486).yield_interest().display_account_info()
account2.deposit(354).deposit(298).withdraw(974).withdraw(974).withdraw(974).withdraw(974).yield_interest().display_account_info()

BankAccount.all_account_info()