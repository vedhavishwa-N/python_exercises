"""Make the above function
more consistent to give the same result whenever same name is given"""
import astrologer


print("enter yes if you want to continue")
next=input()
while next == "yes":
    print("enter your name: ")
    name = input()
    name.lower()
    print(astrologer.get_past_life_v2(name))
    print("enter yes if you want to continue")
    next=input()