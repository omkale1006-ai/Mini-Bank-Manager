# Description:
# Banaye ek simple banking system jisme user account create kar sake, deposit/withdraw kar sake aur balance check kar sake.

# 💡 Features:
# BankAccount class banaye.
# Har account ka account_number, name, aur balance hoga.
# Methods:
# deposit(amount)
# withdraw(amount)
# display_balance()
# display_account_details()
# Extra Challenge (Optional):
# Multiple accounts handle karne ka system banao (list of objects).
# Menu system banao (1. Create Account 2. Deposit 3. Withdraw 4. Check Balance 5. Exit)
class BankAccount:
    def __init__(self, acc_number, name, balance=0):
        self.acc_number = acc_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ ₹{amount} deposited successfully.")
        else:
            print("❌ Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"✅ ₹{amount} withdrawn successfully.")
        else:
            print("❌ Insufficient balance or invalid amount.")

    def display_balance(self):
        print(f"💰 Current Balance: ₹{self.balance}")

    def display_account_details(self):
        print("📋 Account Details:")
        print(f"   Account No: {self.acc_number}")
        print(f"   Name: {self.name}")
        print(f"   Balance: ₹{self.balance}")


# 🔁 List to store multiple accounts
accounts = []

# 🔍 Helper function to find account
def find_account(acc_number):
    for acc in accounts:
        if acc.acc_number == acc_number:
            return acc
    return None

# 📋 Main menu loop
while True:
    print("\n🏦 Welcome to Python Bank 🏦")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Account Details")
    print("6. Exit")

    choice = input("👉 Enter your choice (1-6): ")

    if choice == "1":
        acc_number = input("🔢 Enter account number: ")
        name = input("👤 Enter your name: ")
        balance = float(input("💵 Enter initial balance: "))
        new_acc = BankAccount(acc_number, name, balance)
        accounts.append(new_acc)
        print("✅ Account created successfully.")

    elif choice == "2":
        acc_number = input("🔍 Enter account number: ")
        acc = find_account(acc_number)
        if acc:
            amt = float(input("💰 Enter amount to deposit: "))
            acc.deposit(amt)
        else:
            print("❌ Account not found.")

    elif choice == "3":
        acc_number = input("🔍 Enter account number: ")
        acc = find_account(acc_number)
        if acc:
            amt = float(input("💸 Enter amount to withdraw: "))
            acc.withdraw(amt)
        else:
            print("❌ Account not found.")

    elif choice == "4":
        acc_number = input("🔍 Enter account number: ")
        acc = find_account(acc_number)
        if acc:
            acc.display_balance()
        else:
            print("❌ Account not found.")

    elif choice == "5":
        acc_number = input("🔍 Enter account number: ")
        acc = find_account(acc_number)
        if acc:
            acc.display_account_details()
        else:
            print("❌ Account not found.")

    elif choice == "6":
        print("🙏 Thank you for using Python Bank. Goodbye!")
        break

    else:
        print("⚠️ Invalid option, please try again.")
