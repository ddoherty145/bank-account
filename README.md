Bank Account Simulation
This project demonstrates a simple Bank Account simulation using Python. It includes a BankAccount class that simulates basic bank operations like depositing money, calculating interest, and withdrawing funds. The code also includes examples of creating bank account instances and interacting with them.

Project Files
bank_account.py: Contains the BankAccount class with various methods to perform banking operations and example usage.
README.md: This file provides documentation on how the code works.
Overview of BankAccount Class
The BankAccount class simulates a basic bank account with the following attributes and methods:

Attributes
full_name: The full name of the bank account owner.
account_number: A randomly generated 8-digit unique number for each account.
balance: Represents the current balance of the bank account, starting at $0.00.
Methods
__init__(self, full_name):

Initializes a new bank account with the owner's name, a unique 8-digit account number, and a starting balance of $0.00.
generate_account_number(self):

Generates a random 8-digit account number using Python's random library.
deposit(self, amount):

Takes an amount parameter and adds it to the account balance.
Prints a message indicating the deposited amount and the new balance.
Example: Amount deposited: $100.00 new balance: $100.00
get_balance(self):

Prints a user-friendly message showing the current balance.
Returns the current balance.
Example: Current balance: $100.00
add_interest(self):

Calculates and adds monthly interest to the balance. The interest rate is set at 1% annually (0.083% per month).
Prints a message indicating the interest added and the new balance.
Example: Interest added: $0.83 new balance: $100.83
print_statement(self):

Prints the account details, including the owner's name, account number, and the current balance.
Example:
yaml
Copy code
Account Statement
Owner: John Doe
Account Number: 12345678
Balance: $100.83
withdraw(self, amount):

Withdraws a specified amount from the account if sufficient funds are available.
Prints a message indicating the amount withdrawn and the new balance.
If funds are insufficient, it prints a message indicating the failed transaction.
Example: Amount withdrawn: $50.00 new balance: $50.83
If Balance falls bellow $0 then the account will be charged $10