import random

class Bank:
    def __init__(self):
        self.accounts = {}
        self.loans = {}
        self.transactions = {}
        self.loan_feature_enabled = True  # Loan feature is initially enabled

    def create_account(self, name, email, address, account_type):
        account_number = random.randint(1000, 9999)
        balance = 0
        self.accounts[account_number] = {'name': name, 'email': email, 'address': address, 'type': account_type, 'balance': balance}
        return account_number

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            return f"Account {account_number} has been deleted."
        else:
            return "Account does not exist."

    def get_all_accounts(self):
        return self.accounts

    def check_total_balance(self):
        total_balance = sum(account['balance'] for account in self.accounts.values())
        return total_balance

    def check_total_loan_amount(self):
        total_loan_amount = sum(sum(loans) for loans in self.loans.values())
        return total_loan_amount

    def toggle_loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled
        return "Loan feature has been turned OFF." if not self.loan_feature_enabled else "Loan feature has been turned ON."

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
            return "Loan feature is currently turned OFF."
        
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

    def _add_transaction(self, account_number, transaction):
        if account_number not in self.transactions:
            self.transactions[account_number] = []
        self.transactions[account_number].append(transaction)

class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        return self.bank.create_account(name, email, address, account_type)

    def delete_account(self, account_number):
        return self.bank.delete_account(account_number)

    def get_all_accounts(self):
        return self.bank.get_all_accounts()

    def check_total_balance(self):
        return self.bank.check_total_balance()

    def check_total_loan_amount(self):
        return self.bank.check_total_loan_amount()

    def toggle_loan_feature(self):
        return self.bank.toggle_loan_feature()

# Testing the system
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
        print("10. Admin - List All Accounts")
        print("11. Admin - Total Bank Balance")
        print("12. Admin - Total Loan Amount")
        print("13. Admin - Toggle Loan Feature")
        print("14. Exit")

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

        # Implement other user functions (3-7) similarly

        elif choice == "8":
            name = input("Enter admin name: ")
            email = input("Enter admin email: ")
            address = input("Enter admin address: ")
            account_type = "Admin"
            account_number = admin.create_account(name, email, address, account_type)
            print(f"Admin account created successfully. Your account number is: {account_number}")

        elif choice == "9":
            account_number = int(input("Enter account number to delete: "))
            message = admin.delete_account(account_number)
            print(message)

        elif choice == "10":
            all_accounts = admin.get_all_accounts()
            print("List of All User Accounts:")
            for account_number, account_info in all_accounts.items():
                print(f"Account {account_number}: {account_info['name']} ({account_info['type']})")

        elif choice == "11":
            total_balance = admin.check_total_balance()
            print(f"Total Bank Balance: ${total_balance}")

        elif choice == "12":
            total_loan_amount = admin.check_total_loan_amount()
            print(f"Total Loan Amount: ${total_loan_amount}")

        elif choice == "13":
            message = admin.toggle_loan_feature()
            print(message)

        elif choice == "14":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")
