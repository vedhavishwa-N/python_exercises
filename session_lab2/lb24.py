# Write a function to find and return the largest number out of the given 3 numbers

def find_largest_number (first_number, second_number, third_number):
    if (first_number > second_number) and (first_number > third_number):
        return first_number
    elif (second_number > first_number) and (second_number > third_number):
        return second_number
    else:
        return third_number

#test case

print (find_largest_number (2, 4, 1))