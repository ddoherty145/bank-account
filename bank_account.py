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
        interest = self.balance * 0.00083
        self.balance += interest
        print(f"Interest added: ${interest:.2f} New Balance: ${self.balance:.2f}")

    

account = BankAccount(full_name="David Doherty")
account.deposit(500.32)
account.withdraw(600)
print(f"Account Owner: {account.full_name}")
print(f"Account Number: {account.account_number}")
print(f"Accoount Balance: ${account.balance}")