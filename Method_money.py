# Bank Account Class

class BankAccount:

    # Constructor
    def __init__(self, owner_name, starting_balance):
        self.owner_name = owner_name
        self.balance = starting_balance

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful.")
        print("Deposited:", amount)

    # Method to display account balance
    def display_balance(self):
        print("Account Owner:", self.owner_name)
        print("Account Balance:", self.balance)


# Create a bank account object
account1 = BankAccount("Dan see", 50000)

# Display initial balance
print("--- Initial Account ---")
account1.display_balance()

# Deposit money
account1.deposit(20000)

# Display updated balance
print("\n--- Updated Account ---")
account1.display_balance()