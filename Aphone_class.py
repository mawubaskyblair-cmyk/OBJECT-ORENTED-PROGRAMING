class Phone:
    def __init__(self, brand, storage_capacity):
        self.brand = brand
        self.storage_capacity = storage_capacity

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Storage Capacity: {self.storage_capacity}GB")

    def make_call(self, number):
        print(f"{self.brand} is calling {number}...")
        print("Call connected.\n")


# Create two Phone objects
phone1 = Phone("Samsung", 128)
phone2 = Phone("iPhone", 256)

# Display info and make calls
phone1.display_info()
phone1.make_call("0701234567")

phone2.display_info()
phone2.make_call("0753199621")