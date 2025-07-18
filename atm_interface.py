class ATM:
    def __init__(self):
        # Simulated user database
        self.users = {
            "1234567890": {"pin": "1234", "balance": 10000.0},
            "9876543210": {"pin": "4321", "balance": 5000.0},
        }
        self.current_user = None

    def start(self):
        print("==== Welcome to Python ATM ====")
        if self.authenticate():
            self.show_menu()
        else:
            print("Too many failed attempts. Exiting.")

    def authenticate(self):
        attempts = 3
        while attempts > 0:
            card = input("Enter card number: ").strip()
            pin = input("Enter 4-digit PIN: ")  # <- PIN is now visible

            if card in self.users and self.users[card]["pin"] == pin:
                self.current_user = card
                print("\nLogin successful!\n")
                return True
            else:
                attempts -= 1
                print(f"Invalid card number or PIN. Attempts left: {attempts}\n")
        return False

    def show_menu(self):
        while True:
            print("====== ATM MENU ======")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Select an option (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("\nThank you for using Python ATM. Goodbye!\n")
                break
            else:
                print("Invalid choice. Please select between 1-4.\n")

    def check_balance(self):
        balance = self.users[self.current_user]["balance"]
        print(f"\nYour current balance is: ₹{balance:.2f}\n")

    def deposit(self):
        try:
            amount = float(input("Enter deposit amount (₹): "))
            if amount <= 0:
                print("Amount must be greater than 0.\n")
            else:
                self.users[self.current_user]["balance"] += amount
                print(f"₹{amount:.2f} deposited successfully.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

    def withdraw(self):
        try:
            amount = float(input("Enter withdrawal amount (₹): "))
            current_balance = self.users[self.current_user]["balance"]

            if amount <= 0:
                print("Amount must be greater than 0.\n")
            elif amount > current_balance:
                print("Insufficient balance.\n")
            else:
                self.users[self.current_user]["balance"] -= amount
                print(f"₹{amount:.2f} withdrawn successfully.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

# Run the program
if __name__ == "__main__":
    atm = ATM()
    atm.start()
