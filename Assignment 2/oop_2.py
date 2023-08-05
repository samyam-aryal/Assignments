'''
Build a Python class to represent a simple banking system. Create a class for a
BankAccount, and another for Customer. The BankAccount class should have a
constructor to initialize the account details (account number, balance, account type).
The Customer class should have a constructor to set the customer's details (name,
age, address) and create a BankAccount object for each customer. Implement a
destructor for both classes to display a message when objects are destroyed.
'''

class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __del__(self):
        print(self.name, "has been destroyed.")



class BankAccount(Customer):
    def __init__(self, name, age, address, account_number, balance, account_type):
        super().__init__(name, age, address) 
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def __del__(self):
        print(self.account_number, " has been destroyed.")

    def get_details(self):
        print("\nBank details are: ", self.name, self.age, self.address, self.account_number, self.balance, self.account_type)
        

customer1 = BankAccount("Ram", 25, "Kathmandu", "123", 1000, "Savings")
customer2 = BankAccount("Shyam", 23, "Patan", "789", 5000, "Current")

customer1.get_details()
customer2.get_details()