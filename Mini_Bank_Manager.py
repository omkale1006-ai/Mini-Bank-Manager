class BankAccount:
    def __init__(self, initial_balance):
        self._balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"✅ Deposited: ₹{amount}. New Balance: ₹{self._balance}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"✅ Withdrew: ₹{amount}. New Balance: ₹{self._balance}")
        else:
            print("❌ Insufficient balance or invalid amount.")

    def get_balance(self):
        return self._balance


def verify_pin():
    correct_pin = "1234"
    attempts = 3
    while attempts > 0:
        pin = input("🔐 Enter your 4-digit PIN: ")
        if pin == correct_pin:
            print("✅ PIN verified successfully!\n")
            return True
        else:
            attempts -= 1
            print(f"❌ Incorrect PIN. Attempts left: {attempts}")
    print("🚫 Too many wrong attempts. Exiting.")
    return False


def main():
    print("🏦 Welcome to Python ATM Simulator 🏦\n")
    
    if not verify_pin():
        return
    
    try:
        initial = float(input("💵 Enter initial balance to open your account: ₹"))
    except ValueError:
        print("❌ Invalid input. Please enter a numeric value.")
        return

    account = BankAccount(initial)

    while True:
        print("\n------ 🏧 ATM Menu ------")
        print("1️⃣  Show Balance")
        print("2️⃣  Deposit Money")
        print("3️⃣  Withdraw Money")
        print("4️⃣  Exit")

        choice = input("👉 Enter your choice (1-4): ")

        if choice == '1':
            print(f"💰 Current Balance: ₹{account.get_balance()}")

        elif choice == '2':
            try:
                amt = float(input("💸 Enter amount to deposit: ₹"))
                account.deposit(amt)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == '3':
            try:
                amt = float(input("💸 Enter amount to withdraw: ₹"))
                account.withdraw(amt)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == '4':
            print("👋 Thank you for using our ATM. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please select between 1 to 4 only.")


# Run the program
main()
