import random
class User:
    def __init__(self,name,email,address,account_type,password) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.password = password
        self.account_number =121200600+random.randint(1, 1000)
        self.balance = 0
        self.transaction_history = []
        self.loan_count = 0
        self.total_loan = 0
        
    def deposit(self,amount):
        if bank_admin.isBankrupt:
            print("The bank is bankrupt. You cannot deposit money.")
        else:
            self.balance+=amount
            self.transaction_history.append(f"Deposited ${amount}")
            print(f'{amount} tk deposit Successfuly!')
        
    def withdraw(self,amount):
        if bank_admin.isBankrupt:
            print("The bank is bankrupt. You cannot withdraw money.")
        else:
            if self.balance>=amount:
                self.balance-=amount
                self.transaction_history.append(f"Withdrew ${amount}")
                print(f'{amount} tk Withdraw successfuly!')
            else:
                print("Sorry, you do not have sufficient balance for this withdrawal.")
            
    
    def check_balance(self):
        return f"Available balance: ${self.balance}"
    
    
    def money_transfer(self,recipient, amount):
        if bank_admin.isBankrupt:
            print("The bank is bankrupt. You cannot money transfer.")
        else:
            if recipient:
                if amount <= self.balance:
                    self.balance -= amount
                    recipient.balance += amount
                    self.transaction_history.append(f"Transferred ${amount} to {recipient.name}.")
                    recipient.transaction_history.append(f"Received ${amount} from {self.name}.")
                    print(f"${amount} transferred to {recipient.name} successfully.") 
                else:
                    print("You have not enough money broh.") 
            else:
                print("Account does not exist.")
    
    def check_transaction_history(self):
        return self.transaction_history
    
    def take_loan(self,amount):
        if bank_admin.isBankrupt:
            print("The bank is bankrupt. You cannot take loan.")
        else:
            if bank_admin.isLoan:
                if self.loan_count < 2:
                    self.loan_count += 1
                    self.total_loan+=amount
                    self.balance += amount
                    self.transaction_history.append(f"Loan of ${amount} taken.")
                    print(f"${amount} loan received successfully.") 
                else:
                    print(f"You have already taken 2 time loan.") 
            else:
                print("Loan nity parben na sorry! Contact pleace near bank er sakai")
                
    def __repr__(self) -> str:
        return f"Account Number: {self.account_number}\nName: {self.name}\nEmail: {self.email}\nAddress: {self.address}\nAccount Type: {self.account_type}\nBalance: ${self.balance:.2f}\nLoan: ${self.total_loan:.2f}"

class Admin(User):
    def __init__(self) -> None:
        self.users = []
        self.isBankrupt = False
        self.isLoan = True
          
    def create_account(self,name,email,address,account_type,password) -> None:
        user = User(name, email, address, account_type,password)
        self.users.append(user)
        return user
    
    def login(self,email, password):
        for user in self.users:
            if user.email==email and user.password==password:
                return user
        return None
    
    def delete_account(self, user):
        if user in self.users:
            self.users.remove(user)
    
    def list_accounts(self):
        return self.users
    
    def total_bank_balance(self):
        return sum(user.balance for user in self.users)

    def total_loan_amount(self):
        return sum(user.total_loan for user in self.users)
        
    def set_takeLoan(self,is_Loan):
        self.isLoan = is_Loan
    
    def set_bankruptcy(self, is_bankrupt):
        self.isBankrupt = is_bankrupt


hello = User("Md slla Uddin","mdAla@gmail.com","Chittagong",'Sevingd',"12345")
bank_admin = Admin()
user1 = bank_admin.create_account("Md Ala Uddin", "mdAla@gmail.com", "Chittagong", 'Sevings',"12345")
user2 = bank_admin.create_account("Md kala Uddin", "mdkala@gmail.com", "Chittagong", 'Sevings',"12345")
user3 = bank_admin.create_account("Md vala Uddin", "mdvala@gmail.com", "Chittagong", 'Sevings',"12345")

while True:
    try:
        print("\nBanking Management System")
        print("1. User Panel")
        print("2. Admin Panel")
        print("3. Exit")
    
        choice = input("Select an option: ")

        if choice == "1":
            print("\nUser Panel")
            print("1. Registration")
            print("2. Login")
            print("3. Exit")
    
            option = input("Select an option: ")
        
            if option == "1":
                user_name = input("Enter your name: ")
                user_email = input("Enter your email: ")
                user_address = input("Enter your address: ")
                user_type = input("Enter account type (Savings/Current): ")
                user_pass = input("Enter your password: ")
                user_account = bank_admin.create_account(user_name, user_email, user_address, user_type,user_pass)
        
                while True:
                    print("\nUser Menu")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Check Transaction History")
                    print("5. Take Loan")
                    print("6. Transfer Money")
                    print("7. Log Out")
                    
                    user_choice = input("Select an option: ")

                    if user_choice == "1":
                        amount = float(input("Enter the deposit amount: $"))
                        user_account.deposit(amount)
                    elif user_choice == "2":
                        amount = float(input("Enter the withdrawal amount: $"))
                        user_account.withdraw(amount)
                    elif user_choice == "3":
                        print(f"${user_account.check_balance()}")
                    elif user_choice == "4":
                        print("\nTransaction History:")
                        for transaction in user_account.check_transaction_history():
                            print(transaction)
                    elif user_choice == "5":
                        loan_amount = float(input("Enter the loan amount: $"))
                        user_account.take_loan(loan_amount)
                    elif user_choice == "6":
                        recipient_id = int(input("Enter the recipient's User ID: "))
                        recipient = next((user for user in bank_admin.users if user.account_number == recipient_id), None)
                        if recipient:
                            amount = float(input("Enter the transfer amount: $"))
                            user_account.money_transfer(recipient, amount)
                        else:
                            print("Recipient account does not exist.")
                    elif user_choice == "7":
                        break
                    else:
                        print("Invalid Option")
            elif option =="2":
                user_email = input("Enter your email: ")
                user_pass = input("Enter your password: ")
                user_account = bank_admin.login(user_email,user_pass)
            
                if user_account:
                    print(f'{user_account.name}, your account was successfully logged in!')
                    while True:
                        print("\nUser Menu")
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Check Balance")
                        print("4. Check Transaction History")
                        print("5. Take Loan")
                        print("6. Transfer Money")
                        print("7. Log Out")
                    
                        user_choice = input("Select an option: ")

                        if user_choice == "1":
                            amount = float(input("Enter the deposit amount: $"))
                            user_account.deposit(amount)
                        elif user_choice == "2":
                            amount = float(input("Enter the withdrawal amount: $"))
                            user_account.withdraw(amount)
                        elif user_choice == "3":
                            print(f"${user_account.check_balance()}")
                        elif user_choice == "4":
                            print("\nTransaction History:")
                            for transaction in user_account.check_transaction_history():
                                print(transaction)
                        elif user_choice == "5":
                            loan_amount = float(input("Enter the loan amount: $"))
                            user_account.take_loan(loan_amount)
                        elif user_choice == "6":
                            recipient_id = int(input("Enter the recipient's User ID: "))
                            recipient = next((user for user in bank_admin.users if user.account_number == recipient_id), None)
                            if recipient:
                                amount = float(input("Enter the transfer amount: $"))
                                user_account.money_transfer(recipient, amount)
                            else:
                                print("Recipient account does not exist.")
                        elif user_choice == "7":
                            break
                        else:
                            print("Invaid Option")
                else:
                    print('Login failed. Invalid email or password.')
            elif option == "3":
                break
            else:
                print("Invalid option!")
        elif choice == "2":
            admin_password = input("Enter admin password: ")
            if admin_password == "admin123":
                while True:
                    print("\nAdmin Menu")
                    print("1. Create User Account")
                    print("2. Delete User Account")
                    print("3. List User Accounts")
                    print("4. Total Bank Balance")
                    print("5. Total Loan Amount")
                    print("6. Toggle Loan Feature")
                    print("7. Bankrupt")
                    print("8. Log Out")

                    admin_choice = input("Select an option: ")

                    if admin_choice == "1":
                        try:
                            user_name = input("Enter user's name: ")
                            user_email = input("Enter user's email: ")
                            user_address = input("Enter user's address: ")
                            user_type = input("Enter account type (Savings/Current): ")
                            user_pass = input("Enter your password: ")
                            bank_admin.create_account(user_name, user_email, user_address, user_type,user_pass)
                        except ValueError:
                            print("Invalid Option! Please enter a number.")
                            continue
                    elif admin_choice == "2":
                        try:
                            account_number = int(input("Enter the User ID to delete: "))
                            user_to_delete = next((user for user in bank_admin.users if user.account_number == account_number), None)
                            if user_to_delete:
                                bank_admin.delete_account(user_to_delete)
                                print(f"User ID {account_number} deleted.")
                            else:
                                print("User not found.")
                        except ValueError:
                            print("Invalid Option! Please enter a number.")
                            continue
                        
                    elif admin_choice == "3":
                        try:
                            print("\nUser Accounts:")
                            for user in bank_admin.list_accounts():
                                print(user)
                        except ValueError:
                            print("Invalid Option! Please enter a number.")
                            continue
                    elif admin_choice == "4":
                        print(f"Total Bank Balance: ${bank_admin.total_bank_balance()}")
                    elif admin_choice == "5":
                        print(f"Total Loan Amount: ${bank_admin.total_loan_amount()}")
                    elif admin_choice == "6":
                        while True:
                            print("\nLoan Menu")
                            print("1. Enable")
                            print("2. disable")
                            bankrup_choice = input("Select an option: ")
                            
                            if bankrup_choice=="1":
                                bank_admin.set_takeLoan(True)
                                print("Loan Nity parbeen ")
                                break
                            elif bankrup_choice=="2":
                                bank_admin.set_takeLoan(False)
                                print("Loan Nity parbeen na")
                                break
                    elif admin_choice == "7":
                        while True:
                            print("\nBankrupt Menu")
                            print("1. Yes")
                            print("2. No")
                            bankrup_choice = input("Select an option: ")
                            
                            if bankrup_choice=="1":
                                bank_admin.set_bankruptcy(True)
                                print("Bankruptcy status updated to True (bankrupt).")
                                break
                            elif bankrup_choice=="2":
                                bank_admin.set_bankruptcy(False)
                                print("Bankruptcy status updated to False.")
                                break
                                
                    elif admin_choice == "8":
                        break
            else:
                print("Invalid password. Access denied.")
        elif choice == "3":
            print("Thank you for using the Banking Management System.")
            break
    except ValueError:
        print("Invalid Option! Please enter a number.")
        continue


