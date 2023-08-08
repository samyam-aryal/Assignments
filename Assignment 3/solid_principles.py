#######################################################################################

# SINGLE RESPONSIBILITY PRINCIPLE

# class Book:
#     def __init__(self, title, author, isbn, genre):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.genre = genre
#         self.availability = True

# # Class LibraryCatalog inherits Book class   
# class LibraryCatalog():
#     def __init__(self):
#         self.book_list = []
    
#     def add_book(self, book: Book):
#         self.book_list.append(book)
    
#     def get_book_details(self, book: Book):
#         print(f"\nISBN for {book.title} is ", book.isbn)
#         return book
    
#     def get_book_list(self):
#         print("\n\nBook titles are")
#         for book in self.book_list:
#             print(book.title)
#         # return self.book_list

# class BookBorrower():
#     def __init__(self, library_catalog):
#         self.library_catalog = library_catalog

#     def borrow_book(self, book):
#         if book.availability == True:
#             book.availability = False
#             print("Book borrowed", book.availability)

#     def return_book(self, book):
#         book.availability = True
#         print("Book returned", book.availability)
        

# book1 = Book("To Kill a Mockingbird", "Harper Lee", "1", "Fiction")
# book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "2", "Fantasy")
# book3 = Book("The Kite Runner", "Khaled Hosseini", "3", "Non-fiction")

# library_catalog = LibraryCatalog()
# library_catalog.add_book(book1)
# library_catalog.add_book(book2)
# library_catalog.add_book(book3)
# library_catalog.get_book_details(book1)
# library_catalog.get_book_details(book2)
# library_catalog.get_book_details(book3)
# library_catalog.get_book_list()

# borrow = BookBorrower(library_catalog)
# borrow.borrow_book(book1)
# borrow.return_book(book1)


#######################################################################################

# OPEN/ CLOSE PRINCIPLE

# Software entities (classes, modules, functions, etc.) should be
# open for extension, but closed for modification.”


# from abc import ABC, abstractmethod

# class Product:
#     def __init__(self, price):
#         self.price = price

# class Price(ABC):
#     @abstractmethod
#     def calculate_total_price(self, products: list):
#         pass

# class Total_Price(Price):
#     def calculate_total_price(self, products: list):
#         total_price = 0
#         for product in products:
#             total_price += product.price
#         # print("Total price is ", total_price)
#         return total_price

# class Discounted_Price(Price):
#     def calculate_total_price(self, products: list):
#         total_price = 0
#         for product in products:
#             total_price += product.price
#         total_price = total_price * (1-20/100)
#         # print("\n\n Discounted price is ", total_price)
#         return total_price

#######################################################################################

# Liskov Substitution Principle

# Objects of a superclass should be replaceable with objects of its subclasses without breaking the application
# Objects of the subclass should behave in the same way as the objects of the superclass


# For the Saving and Checking accounts to follow LSP, their behaviors must be the same.
# So, we make the 'withdraw' method act the saame way for both accounts, and inherit that method from
# the superclass 'Account'. We then ensure that overdrafts are enabled in the Checking accounts by 
# creating a total_balance variable that takes into account the overdraft limit while allowing withdrawals. 

class Account():
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rs{amount}. Remaining balance: Rs{self.balance}")
        else:
            print("Insufficient funds!")


class SavingsAccount(Account):
    pass


class CheckingAccount(Account):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        total_balance = self.balance + self.overdraft_limit
        if amount <= total_balance:
            self.balance -= amount
            print(f"Withdrew Rs{amount}. Remaining balance: Rs{self.balance}")
        else:
            print("Exceeds overdraft limit or insufficient funds!")

def perform_bank_actions(account):
    account.withdraw(100)
    account.withdraw(200)
    account.withdraw(500)

savings_account = SavingsAccount(500)
checking_account = CheckingAccount(1000, 200)

savings_account.withdraw(100)
savings_account.withdraw(500)

checking_account.withdraw(1000)
checking_account.withdraw(200)
checking_account.withdraw(500)

#######################################################################################

# Interface Segregation Principle
# ISP 

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class RefundProcessor(ABC):
    @abstractmethod
    def process_refund(self, amount):
        pass

class OnlinePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

class OnlineRefundProcessor(RefundProcessor):
    def process_refund(self, amount):
        print(f"Processing refund of ${amount}")

def process_payments(payment_processor, amount):
    payment_processor.process_payment(amount)

def process_refunds(refund_processor, amount):
    refund_processor.process_refund(amount)

if __name__ == "__main__":
    online_payment_processor = OnlinePaymentProcessor()
    online_refund_processor = OnlineRefundProcessor()

    # Process payments and refunds
    process_payments(online_payment_processor, 100)
    process_refunds(online_refund_processor, 50)

#######################################################################################

# Dependency Inversion Principle

# “Abstractions should not depend upon details. Details
# should depend upon abstractions.”

from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send_message(self, recipient, message):
        pass

class EmailSender(MessageSender):
    def send_message(self, recipient, message):
        # Code to send an email
        print(f"Sending email to {recipient}: {message}")

class NotificationService:
    def __init__(self, message_sender):
        self.message_sender = message_sender

    def send_notification(self, recipient, message):
        self.message_sender.send_message(recipient, message)

# Using the NotificationService to send a notification
if __name__ == "__main__":
    email_sender = EmailSender()
    notification_service = NotificationService(email_sender)
    notification_service.send_notification("user@example.com", "Hello, this is a notification!")
