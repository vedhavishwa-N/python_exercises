# Write a function to find if a given number a is divisible by another given number b.
#  - For example, is_divisible(a,b)

def divisibe (dividend, divisor):
    check = dividend/ divisor
    if check == int(check):
        return "{} is divisible by {} ".format (dividend, divisor)
    else:
        return "{} is not divisible by {} ".format (dividend, divisor)

# test case

print (divisibe (3, 4))
