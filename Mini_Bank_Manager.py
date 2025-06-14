class BankAccount:
    def __init__(self, initial_balance):
        self._balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: {amount}. New balance: {self._balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self._balance


def main():
    initial = float(input("Enter initial balance: ₹"))
    account = BankAccount(initial)

    while True:
        print("\n------ Bank Menu ------")
        print("1. Show Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Exit Program")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"Current Balance: ₹{account.get_balance()}")

        elif choice == '2':
            amt = float(input("Enter amount to deposit: ₹"))
            account.deposit(amt)

        elif choice == '3':
            amt = float(input("Enter amount to withdraw: ₹"))
            account.withdraw(amt)

        elif choice == '4':
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice. Please enter 1 to 4 only.")


# Run the program
main()
