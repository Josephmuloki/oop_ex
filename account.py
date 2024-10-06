class BankAccount:# Defines the class
    # Class variable shared by all instances
    interest_rate = 0.05

    def __init__(self, account_holder):# Initializes new instance
        # Instance variables unique to each instance
        self.account_holder = account_holder #Sets the account holder’s name.
        self.balance = 0  # Initial balance set to zero

    def deposit(self, amount): #Defines the method to deposit money.
        # Adds the specified amount to the balance
        self.balance += amount #Adds the deposit amount to the balance.
        print(f"Deposited {amount}. New balance is {self.balance}.") #Prints the new balance after deposit.

    def withdraw(self, amount):#Defines the method to withdraw money.
        # Checks if there are sufficient funds to withdraw
        if amount <= self.balance:#Checks if there are sufficient funds.
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")  # Message if funds are insufficient

    def apply_interest(self):
        # Calculates interest based on the current balance and interest rate
        interest = self.balance * BankAccount.interest_rate #Calculates the interest based on the current balance.
        self.balance += interest  # Adds the interest to the balance
        print(f"Applied interest {interest}. New balance is {self.balance}.")

    def display_account_info(self):
        # Displays the account holder's name and current balance
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

# Creating two instances of BankAccount
account1 = BankAccount("Muloki")
account2 = BankAccount("Joseph")

# Performing deposits and withdrawals for the first account
account1.deposit(1000)  # Deposits 1000 to Muloki's account
account1.withdraw(200)  # Withdraws 200 from Muloki's account
account1.apply_interest()  # Applies interest to Muloki's account
account1.display_account_info()  # Displays Muloki's account information

# Performing deposits and withdrawals for the second account
account2.deposit(500)  # Deposits 500 to Joseph's account
account2.withdraw(100)  # Withdraws 100 from 's account
account2.apply_interest()  # Applies interest to Joseph's account
account2.display_account_info()  # Displays Joseph's account information
