import random

class BankAccount:
    def __init__(self, full_name):
        self.full_name = full_name
        self.account_number = self.generate_account_number()
        self.balance = 0

    def generate_account_number(self):
        #generate a random 8-digit num
        return random.randint(10000000, 99999999)
    
    def deposit(self, amount):
        #add deposit to amount
        self.balance += amount
        print(f"Amount deposited: ${amount:.2f} new balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        #withdraw from amount
        self.balance -= amount
        if self.balance <= 0:
            print("Insufficient Funds.")
            self.balance -= 10 #overdarft fee
        else:
            print(f"Amount withdrawn: ${amount:.2f}, new balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
        return self.balance
    
    def add_interest(self):
        interest = self.balance * 0.00083 #interest added
        self.balance += interest
        print(f"Interest added: ${interest:.2f} New Balance: ${self.balance:.2f}")

    def print_statement(self):
        print(f"Account Statement\nOwner: {self.full_name}\nAccount Number: {self.account_number}\nBalance: ${self.balance:.2f}")

    

# account = BankAccount(full_name="David Doherty")
# account.deposit(500.32)
# account.withdraw()
# account.get_balance()
# account.add_interest()
# account.print_statement()
# print(f"Account Owner: {account.full_name}")
# print(f"Account Number: {account.account_number}")
# print(f"Accoount Balance: ${account.balance}")

david_account = BankAccount(full_name="David")
tiffany_account = BankAccount(full_name="Tiffany")
kae_account = BankAccount(full_name="Kae")

david_account.deposit(40000)
david_account.withdraw(1000)

tiffany_account.deposit(50000)
tiffany_account.add_interest()
tiffany_account.print_statement()

kae_account.deposit(60000)
kae_account.get_balance()

#added mitchell's account
mitchell_account = BankAccount(full_name="Mitchell")
# mitchell_account.account_number = 3141592
mitchell_account.account_number = "{:08d}".format(3141592)

mitchell_account.deposit(400000)
mitchell_account.print_statement()

mitchell_account.add_interest()
mitchell_account.print_statement()

mitchell_account.withdraw(150)
mitchell_account.print_statement()
