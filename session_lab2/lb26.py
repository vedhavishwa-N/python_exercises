"""Write a function to find the selling price of the book when the list price is given.
 For the purpose of this problem assume that the discount is 10%"""

def selling_price_of_book (list_price):
    selling_price = list_price - (list_price * 10 / 100)
    return selling_price

# test cases

print (selling_price_of_book (1000))

