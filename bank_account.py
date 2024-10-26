import random

class BankAccount:
    def __init__(self, full_name):
        self.full_name = full_name
        self.account_number = self.generate_account_number()
        self.balance = 0

    def generate_account_number(self):
        #generate a random 8-digit num
        return random.randint(10000000, 99999999)
    

account = BankAccount(full_name="David Doherty")
print(f"Account Owner: {account.full_name}")
print(f"Account Number: {account.account_number}")
print(f"Accoount Balance: ${account.balance}")