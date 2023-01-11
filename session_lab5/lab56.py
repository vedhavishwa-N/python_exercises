"""Enhance the program you have written for session 4 -
Problem 6, 7 and 8 to use the concept of classes.
The functionality to provide the past life details and the predictions
should now be included in a class called Astrologer.
 Here are the additional enhancements you need to make:
Please use dicts to store the past lives found earlier
in a dict for the sake of maintaining consistency.
Please do the same for predictions as well.
That means once a prediction is given for a specific name input,
the program should continue to give the same prediction for the same name.
"""

import Class_astrologer

on = "yes"


while on == "yes":
   print ("enter past or future which you want to know ")
   start = input ()

   if start == "past":
        name = input ("enter your name: ")
        NAME = Class_astrologer.Astrologer (name)
        NAME.get_past_life ()
        on = input ("enter yes if you want to try again")

   elif start == "future":
       name = input("enter your name: ")
       NAME = Class_astrologer.Astrologer (name)
       NAME.get_next_life ()
       on = input ("enter yes if you want to try again")

   else:
       print ("enter a valid input")
       on = input ("enter yes if you want to try again : ")
