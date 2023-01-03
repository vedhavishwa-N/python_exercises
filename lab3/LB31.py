"""Write a function to find the selling price of the book when the list price
and discount_percentage are given. Discount percentage should be optional.
When no value is provided, the function will assume that the value is 10%
"""
# sample program
"""def sell_price( list_price, discount):
    #if (list_price > 0):
    list_price= list_price - (list_price*(discount/100))
    #else:
    print("the book is free")
    return list_price
print("enter the list price  ")
l_p=eval(input())
print("enter the discount value if any ")
d=input()
if d!="":
    d=eval(d)
else:
    d=10
print("the selling price of book is ",sell_price(l_p,d))"""

def sell_price(list_price, discount):
    if discount !="":
        discount=eval(discount)
        list_price= list_price - (list_price*(discount/100))
    else:
        discount=10
        list_price = list_price - (list_price * (discount / 100))
    return list_price
print("enter the list price  :")
l_p=eval(input())
print("enter the discount value if any else enter 0 :")
d=input()
print("the selling price of book is ",sell_price(l_p,d))