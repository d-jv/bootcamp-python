class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

        #----------------codigo de Moriak -------------------------
        # self.accounts = {1: BankAccount(0.02, 0)}
        # def new_account(self, cod, int_rate=0.02, amount=0):
        # self.accounts[cod] = BankAccount(int_rate, amount)
        # return self
        #----------------FIN codigo de Moriak -------------------------
        #----------------codigo de Rodrigo Marquez -------------------------
        # class User:
        #     def __init__(self,name,email):
        #         self.name = name
        #         self.email = email
        #         self.account = [BankAccount(0.05)]
        #     def make_deposit(self,amount,num):
        #         self.account[num].deposit(amount)
        #         return self
        #     def create_account(self):
        #         self.account.append(BankAccount(0.05))
        #----------------FIN codigo de Rodrigo Marquez -------------------------

    def make_deposit(self, amount):	
        self.account.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self
    def display_user_balance(self):
        print(f'Usuario: {self.name}, Saldo: {self.account.balance}')
        return self
    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        self.display_user_balance()
        other_user.display_user_balance()


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

# ayuwoki = User('Ayuwoki', 'ayuwoki@heehee.com')
# johnDoe = User('John Doe', 'john@doe.com')
# nameless = User('Nameless', 'nameless@noname.com')

johnDoe = User('John Doe', 'john@doe.com')
johnDoe.account.deposit(444)
johnDoe.make_deposit(15000).make_deposit(10000).make_deposit(50000).make_withdrawal(32000).display_user_balance()