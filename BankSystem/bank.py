class BankAccount:
    account_counter = 1000

    def __init__(self, owner, pin, balance=0):
        self.owner = owner
        self.__pin = pin
        self.__balance = balance
        self.account_number = BankAccount.account_counter
        BankAccount.account_counter += 1
        self.history = []

    def verify_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount, note="Deposited"):
        if amount > 0:
            self.__balance += amount
            self.history.append(f"{note} {amount}")
        else:
            print("Invalid amount. Amount should be greater than zero.")

    def withdraw(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance -= amount
            self.history.append(f"Withdrew {amount}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

    def show_history(self):
        if not self.history:
            print("No transaction history.")
        else:
            for entry in self.history:
                print(entry)

    def __str__(self):
        return f"Account #{self.account_number} - Owner: {self.owner}, Balance: {self.__balance}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, pin, balance=0, interest_rate=0.03):
        super().__init__(owner, pin, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest, note="Interest Applied:")


def main():
    accounts = []

    while True:
        print("\nWelcome to your bank!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")  # ✅ Treat input as string

        if choice == '1':
            name = input("Enter your name: ")
            pin = input("Enter your secret pin: ")
            acc_type = input("Account type (savings): ").lower()

            if acc_type == "savings":
                account = SavingsAccount(name, pin)
            else:
                print("Only 'savings' accounts supported for now.")
                continue

            accounts.append(account)
            print(f"Account created. Your number is {account.account_number}")

        elif choice == '2':
            try:
                acc_num = int(input("Enter account number: "))
                pin = input("Enter PIN: ")
            except ValueError:
                print("Invalid input.")
                continue

            account = next((a for a in accounts if a.account_number == acc_num), None)

            if account and account.verify_pin(pin):
                print(f"Welcome, {account.owner}")
                while True:
                    print("\n1. Deposit\n2. Withdraw\n3. Balance\n4. History\n5. Apply Interest\n6. Logout")
                    action = input("Choose action: ")

                    if action == '1':
                        try:
                            amt = float(input("Amount to deposit: "))
                            account.deposit(amt)
                        except ValueError:
                            print("Invalid amount.")
                    elif action == '2':
                        try:
                            amt = float(input("Amount to withdraw: "))
                            account.withdraw(amt)
                        except ValueError:
                            print("Invalid amount.")
                    elif action == '3':
                        print("Balance:", account.get_balance())
                    elif action == '4':
                        account.show_history()
                    elif action == '5':
                        if isinstance(account, SavingsAccount):
                            account.apply_interest()
                        else:
                            print("Interest not supported for this account type.")
                    elif action == '6':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid option.")
            else:
                print("Account not found or wrong PIN.")

        elif choice == '3':
            print("Thank you for using our banking system.")
            break
        else:
            print("Invalid menu option.")


if __name__ == "__main__":
    main()
