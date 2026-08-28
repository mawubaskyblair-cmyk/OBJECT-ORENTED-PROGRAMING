class BankAccount:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_info(self):
        print(f"Owner: {self.owner_name}")
        print(f"Balance: {self.balance}")


# Create accounts
account1 = BankAccount("Mawuba", 5000)
account2 = BankAccount("sky")  # uses default balance of 0

# Use the accounts
account1.display_info()
account1.deposit(2000)
account1.withdraw(1000)

print()

account2.display_info()
account2.deposit(1500)
account2.withdraw(3000)  # will fail — insufficient funds