class Book (object):
    def __init__ (self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__ (self):
        return "the book {} written by {} is worth {}".format (self.title, self.author, self.price)


book = Book ("About India", "jagan", 500.00)
book1 = Book ("About Chennai", "Jayan", 400.50)

print (book)
print (book1)

