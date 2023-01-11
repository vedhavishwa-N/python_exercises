# Write a function to find if a given character is a vowel ( should return boolean value )

def vowel_checker (given_character):
    vowels= ['a', "e", "i", "o", "u"]
    if given_character in vowels:
        return True
    else:
        return False

#test cases

print ("\n",vowel_checker ("a"))
print ("\n",vowel_checker (" b"))


