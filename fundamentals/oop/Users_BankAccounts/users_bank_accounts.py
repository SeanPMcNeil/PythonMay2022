from re import A


class User:

    def __init__(self, name, account_type):
        self.name = name
        self.account = BankAccount(account_type, int_rate = 2, balance = 0)

    def make_deposit(self, amount, account_type):
        self.account.deposit(account_type, amount) 

    def make_withdrawal(self, amount, account_type):
        self.account.withdraw(account_type, amount)

    def display_user_balance(self, account_type):
        print(f"User: {self.name}, {self.account.display_account_info(account_type)}")


class BankAccount:
    all_accounts = []
    balance = {}

    def __init__(self, account_type, int_rate, balance): 
        self.int_rate = int_rate
        self.balance[account_type] = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount, account_type):
        self.balance[account_type] += amount
        return self

    def withdraw(self, amount, account_type):
        if (self.balance[account_type] - amount < 0):
            print("Insufficient funds: Charging a $5 fee")
            self.balance[account_type] -= 5
        else:
            self.balance[account_type] -= amount
        return self

    def display_account_info(self, account_type):
        return f"{account_type} Balance: ${self.balance[account_type]}"

    def yield_interest(self, account_type):
        if self.balance[account_type] > 0:
            self.balance[account_type] *= (1 + (.01 * self.int_rate))
        return self

    @classmethod
    def all_account_info(cls):
        for account in cls.all_accounts:
            print(f"Balance: ${account.balance}")

sean = User('Sean', 'Checking')
sean = User('Sean', 'Savings')

sean.account.deposit(2500, 'Checking')
sean.account.deposit(3750, 'Savings')
# Checking Method Chaining
sean.account.deposit(2500, 'Checking').deposit(2500, 'Checking').deposit(2500, 'Checking').deposit(2500, 'Checking')
sean.account.deposit(5500, 'Savings').deposit(5500, 'Savings').deposit(5500, 'Savings')
# Checking Chaining with changing accounts
sean.account.withdraw(375, 'Checking').withdraw(375, 'Savings').withdraw(375, 'Checking').withdraw(375, 'Savings')

sean.account.yield_interest('Savings')

sean.display_user_balance('Checking')
sean.display_user_balance('Savings')