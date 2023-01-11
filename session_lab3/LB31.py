"""Write a function to find the selling price of the book when the list price
and discount_percentage are given. Discount percentage should be optional.
When no value is provided, the function will assume that the value is 10%
"""
# funtion declaration
def sell_price (list_price, discount = 10):
    # if condition to check if there is a discount
    if discount != 10:
        list_price = list_price - (list_price* ( discount / 100))
    else:
    # default 10 % discount    
        list_price = list_price - ( list_price * ( discount / 100))
    return "the selling price of book is {}".format (list_price)

# test case

print (sell_price (500))
print (sell_price (500, 20))