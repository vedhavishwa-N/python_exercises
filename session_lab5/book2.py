"""
Let us create a class/data type called Book.
A bookstore software is going to use this class ( or data type ) 

What kind of data are we going to store in the object? ( What are the attributes of the object? )

title - str
author - str
isbn - str 
price - float
stock - int

What kind of operations ( methods ) do we want to perform on the object? ( What methods do we want to support? )

sell
refill

"""

class Book (object):
    def __init__ (self, title, author, isbn, price, stock):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.stock = stock

    def sell (self, copies):
        self.stock = self.stock - copies

    def refill (self, copies):
        self.stock = self.stock + copies

    def __str__ (self):
        return "title - {}, copies - {}".format (self.title, self.stock)


book1 = Book("About India", "vedha", "1234567890123", 500.99, 100)
print(book1)

operation = input("What do you want to do? (S-sell|R-refill) enter in caps either S or R ")
if operation == "S":
    copies = eval (input ("How many copies do you want to sell? "))
    book1.sell (copies)
    print ("Thanks. Now you have {} copies left ".format (book1.stock))

elif operation == "R":
    copies = eval (input ("How many copies do you want to refill? "))
    book1.refill (copies)
    print ("Thanks. Now you have {} copies in stock ".format (book1.stock))

else:
    print ("Sorry, I don't know what you are trying to do! Bye")




