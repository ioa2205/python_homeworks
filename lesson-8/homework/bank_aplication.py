import json
import random

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount. Ensure it's positive and within balance.")

    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            print("Initial deposit must be non-negative.")
            return
        account_number = str(random.randint(10000, 99999))
        while account_number in self.accounts:
            account_number = str(random.randint(10000, 99999))
        
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        print(f"Account created successfully! Your account number: {account_number}")
        self.save_to_file()

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}")
            print(f"Name: {account.name}")
            print(f"Balance: ${account.balance}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def save_to_file(self):
        data = {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}
        with open("accounts.txt", "w") as file:
            json.dump(data, file)

    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as file:
                data = json.load(file)
                self.accounts = {acc_num: Account(acc_num, acc["name"], acc["balance"]) for acc_num, acc in data.items()}
        except FileNotFoundError:
            self.accounts = {}

# Main menu function
def main():
    bank = Bank()
    
    while True:
        print("\nWelcome to the Bank")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank.create_account(name, initial_deposit)
        elif choice == "2":
            acc_num = input("Enter account number: ")
            bank.view_account(acc_num)
        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(acc_num, amount)
        elif choice == "4":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(acc_num, amount)
        elif choice == "5":
            print("Thank you for using the Bank!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
