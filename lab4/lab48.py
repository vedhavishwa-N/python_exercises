"""Enhance the above module and add a function called get_next_life.
 These predictions should be picked up from a list of 3 random strings.
  Prediction strings can be reused. No consistency expected from predictions for the same person.
"""
import astrologer
print("enter your name: ")
name = input()
name.lower()
print(astrologer.get_next_life(name))
