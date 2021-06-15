class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f'Fondos en la cuenta: {self.balance}')
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance = self.balance * (self.int_rate+1)
        else: print('Insufficient funds')
        return self

account1 = BankAccount(0.01, 100000)
account2 = BankAccount(0.01)

account1.deposit(5000).deposit(10000).deposit(5000).withdraw(5000).yield_interest().display_account_info()
account2.deposit(50000).deposit(50000).withdraw(10000).withdraw(5000).withdraw(5000).withdraw(5000).yield_interest().display_account_info()