import random

class Bank:
    def __init__(self):
        self.accounts = {}
        self.loans = {}
        self.transactions = {}
        self.loan_feature_enabled = True

    def create_account(self, name, email, address, account_type):
        account_number = random.randint(1000, 9999)
        balance = 0
        self.accounts[account_number] = {'name': name, 'email': email, 'address': address, 'type': account_type, 'balance': balance}
        return account_number

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            if account_number in self.loans:
                del self.loans[account_number]
            if account_number in self.transactions:
                del self.transactions[account_number]
            return f"Account {account_number} deleted successfully."
        else:
            return "Account does not exist."

    def list_accounts(self):
        return self.accounts

    def total_balance(self):
        total = sum(account['balance'] for account in self.accounts.values())
        return total

    def total_loans(self):
        total = sum(sum(loan_list) for loan_list in self.loans.values())
        return total

    def enable_loan_feature(self):
        self.loan_feature_enabled = True
        return "Loan feature enabled."

    def disable_loan_feature(self):
        self.loan_feature_enabled = False
        return "Loan feature disabled."

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            self._add_transaction(account_number, f'Deposit: +${amount}')
        else:
            return "Account does not exist."

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount <= self.accounts[account_number]['balance']:
                self.accounts[account_number]['balance'] -= amount
                self._add_transaction(account_number, f'Withdrawal: -${amount}')
            else:
                return "Withdrawal amount exceeded."
        else:
            return "Account does not exist."

    def check_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]['balance']
        else:
            return "Account does not exist."

    def transaction_history(self, account_number):
        if account_number in self.transactions:
            return self.transactions[account_number]
        else:
            return "Account does not exist."

    def take_loan(self, account_number, amount):
        if not self.loan_feature_enabled:
            return "Loan feature is currently disabled."
        if account_number in self.accounts:
            if account_number in self.loans and len(self.loans[account_number]) >= 2:
                return "You have reached the maximum number of loans (2)."
            else:
                if account_number not in self.loans:
                    self.loans[account_number] = []
                self.accounts[account_number]['balance'] += amount
                self._add_transaction(account_number, f'Loan: +${amount}')
                self.loans[account_number].append(amount)
                return f'Loan of ${amount} granted.'
        else:
            return "Account does not exist."

    def transfer(self, sender_account, receiver_account, amount):
        if sender_account in self.accounts and receiver_account in self.accounts:
            if amount <= self.accounts[sender_account]['balance']:
                self.accounts[sender_account]['balance'] -= amount
                self.accounts[receiver_account]['balance'] += amount
                self._add_transaction(sender_account, f'Transfer: -${amount} to Account {receiver_account}')
                self._add_transaction(receiver_account, f'Transfer: +${amount} from Account {sender_account}')
            else:
                return "Insufficient funds for the transfer."
        else:
            return "One or both accounts do not exist."

    def _add_transaction(self, account_number, transaction):
        if account_number not in self.transactions:
            self.transactions[account_number] = []
        self.transactions[account_number].append(transaction)

class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        account_number = self.bank.create_account(name, email, address, account_type)
        return account_number

    def delete_account(self, account_number):
        return self.bank.delete_account(account_number)

    def list_accounts(self):
        return self.bank.list_accounts()

    def total_balance(self):
        return self.bank.total_balance()

    def total_loans(self):
        return self.bank.total_loans()

    def enable_loan_feature(self):
        return self.bank.enable_loan_feature()

    def disable_loan_feature(self):
        return self.bank.disable_loan_feature()

if __name__ == '__main__':
    bank = Bank()
    admin = Admin(bank)

    while True:
        print("\nBanking Management System")
        print("1. User - Create Account")
        print("2. User - Deposit")
        print("3. User - Withdraw")
        print("4. User - Check Balance")
        print("5. User - Transaction History")
        print("6. User - Take a Loan")
        print("7. User - Transfer Money")
        print("8. Admin - Create Account")
        print("9. Admin - Delete Account")
        print("10. Admin - List Accounts")
        print("11. Admin - Total Balance")
        print("12. Admin - Total Loans")
        print("13. Admin - Enable Loan Feature")
        print("14. Admin - Disable Loan Feature")
        print("15. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter your account type (Savings/Current): ")
            account_number = bank.create_account(name, email, address, account_type)
            print(f"Account created successfully. Your account number is: {account_number}")

        elif choice == "2":
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter the amount to deposit: "))
            bank.deposit(account_number, amount)
            print(f"Deposited ${amount} successfully.")

        elif choice == "3":
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter the amount to withdraw: "))
            bank.withdraw(account_number, amount)

        elif choice == "4":
            account_number = int(input("Enter your account number: "))
            balance = bank.check_balance(account_number)
            print(f"Available balance: ${balance}")

        elif choice == "5":
            account_number = int(input("Enter your account number: "))
            history = bank.transaction_history(account_number)
            print(f"Transaction History for Account {account_number}:\n{history}")

        elif choice == "6":
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter the loan amount: "))
