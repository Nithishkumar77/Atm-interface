class User:
    def __init__(self, user_id, pin, balance=1000):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        return f"Your balance is ${self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. Your new balance is ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. Your new balance is ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Invalid withdrawal amount."

    def transfer(self, amount, recipient):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient}")
            return f"Transferred ${amount} to {recipient}. Your new balance is ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Invalid transfer amount."

def authenticate_user(users):
    user_id = input("Enter your User ID: ")
    pin = input("Enter your PIN: ")

    if user_id in users and users[user_id].pin == pin:
        return users[user_id]
    else:
        print("Invalid User ID or PIN. Access denied.")
        return None

def main():
    users = {
        "user1": User("user1", "1234"),
        "user2": User("user2", "5678", 1500),
    }

    authenticated_user = authenticate_user(users)

    if authenticated_user:
        while True:
            print("\nOptions:")
            print("1. Transaction History")
            print("2. Check Balance")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Transfer")
            print("6. Quit")

            choice = input("Select an option: ")

            if choice == "1":
                print("\nTransaction History:")
                for transaction in authenticated_user.transaction_history:
                    print(transaction)
            elif choice == "2":
                print(authenticated_user.check_balance())
            elif choice == "3":
                amount = float(input("Enter the deposit amount: $"))
                print(authenticated_user.deposit(amount))
            elif choice == "4":
                amount = float(input("Enter the withdrawal amount: $"))
                print(authenticated_user.withdraw(amount))
            elif choice == "5":
                recipient = input("Enter recipient's name: ")
                amount = float(input(f"Enter the transfer amount to {recipient}: $"))
                print(authenticated_user.transfer(amount, recipient))
            elif choice == "6":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
