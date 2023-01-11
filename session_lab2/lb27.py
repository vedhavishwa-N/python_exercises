"""Extend the above function to take 2  more arguments  discount_percentage and binding_type. 
If binding_type is "HB" no discount is applicable 
even if the discount percentage is provided as an argument.
There is no default discount %age."""

def selling_price_of_book (list_price, discount_percentage, binding_type):
    if binding_type == "HB":
        selling_price = list_price
    else:
        selling_price = list_price - (list_price * discount_percentage / 100)
    return selling_price

# test cases

print (selling_price_of_book (100, 20, "HB"))
print (selling_price_of_book (100, 20, "HM"))
