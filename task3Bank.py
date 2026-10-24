# Create a "BankAccount" class to simulate basic banking operations.

# Requirements:

# - Define attributes for account number, account holder name, and balance.
# - Implement methods to deposit money, withdraw money, and check the current balance.
# - Prevent withdrawals that exceed the available balance.
# - Do not allow negative deposit or withdrawal amounts.
# - Create an object and demonstrate all the operations.

class BankAccount:
    account_number = None
    account_holderName = None
    Balance = None

    def details(self, accountnumber, accountholdername, balance):
        self.account_number = accountnumber
        self.account_holderName = accountholdername
        self.Balance = balance

    def deposit_money(self, balance):
        self.Balance = self.Balance + balance
        print("Your balance now is:", self.Balance)

    def withdraw_money(self, balance):
        if self.Balance >= balance:
            self.Balance = self.Balance - balance
            print("Withdrawn success")
            print("Your current Balance is:", self.Balance)
        else:
            print("Not enough balance in account")

    def check_balance(self):
        print("Your current Balance is:", self.Balance)


User1 = BankAccount()
User1.details(1, "Ram", 2500)
User1.deposit_money(200)
User1.withdraw_money(500)
User1.check_balance()