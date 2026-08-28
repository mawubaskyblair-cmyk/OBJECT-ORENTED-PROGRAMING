# Bank Account Class

class BankAccount:
    def __init__(self, owner_name, starting_balance):
        self.owner_name = owner_name
        self.balance = starting_balance

    # Method to display account information
    def display_account(self):
        print("Owner's Name:", self.owner_name)
        print("Balance:", self.balance)


# Create a bank account object
account1 = BankAccount("John Doe", 500000)

# Display account information
print("--- Bank Account Information ---")
account1.display_account()