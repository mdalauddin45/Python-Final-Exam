import random

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = random.randint(100000, 999999)
        self.balance = 0
        self.transaction_history = []
        self.loan_count = 0
        

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")
        return f"${amount} deposited successfully."

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"${amount} withdrawn successfully."
        else:
            return "Withdrawal amount exceeded."

    def check_balance(self):
        return f"Available balance: ${self.balance}"

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_count < 2:
            self.loan_count += 1
            self.balance += amount
            self.transaction_history.append(f"Loan of ${amount} taken.")
            return f"${amount} loan received successfully."
        else:
            return "You have already taken the maximum number of loans."

    def transfer(self, recipient, amount):
        if recipient:
            if amount <= self.balance:
                self.balance -= amount
                recipient.balance += amount
                self.transaction_history.append(f"Transferred ${amount} to {recipient.name}.")
                recipient.transaction_history.append(f"Received ${amount} from {self.name}.")
                return f"${amount} transferred to {recipient.name} successfully."
            else:
                return "Insufficient funds to transfer."
        else:
            return "Account does not exist."

