class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):	
        self.account_balance += amount	
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f'Usuario: {self.name}, Saldo: {self.account_balance}')
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()

ayuwoki = User('Ayuwoki', 'ayuwoki@heehee.com')
johnDoe = User('Jhon Doe', 'jhon@doe.com')
nameless = User('Nameless', 'nameless@noname.com')

#Haz que el primer usuario haga 3 depósitos y 1 retiro y luego muestre su saldo
ayuwoki.make_deposit(15000)
ayuwoki.make_deposit(10000)
ayuwoki.make_deposit(50000)
ayuwoki.make_withdrawal(32000)
ayuwoki.display_user_balance()

#Haz que el segundo usuario haga 2 depósitos y 2 retiros y luego muestre su saldo
johnDoe.make_deposit(123000)
johnDoe.make_deposit(2000)
johnDoe.make_withdrawal(5000)
johnDoe.make_withdrawal(20000)
johnDoe.display_user_balance()

#Haz que el tercer usuario haga 1 depósitos y 3 retiros y luego muestre su saldo
nameless.make_deposit(250000)
nameless.make_withdrawal(20000)
nameless.make_withdrawal(20000)
nameless.make_withdrawal(10000)
nameless.display_user_balance()

#BONIFICACIÓN: Agrega un método transfer_money; haga que el primer usuario transfiera dinero al tercer usuario y luego imprima los saldos de ambos usuarios
ayuwoki.transfer_money(nameless, 5000)


