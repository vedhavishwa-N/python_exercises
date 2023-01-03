"""Write a class called "Linguist" with the following methods:
1----analyze_text - When a string is given as input,
 the method should return the length of the string,
 total number of words and total number of characters,
  total number of unique words and total number of unique characters
   found in the text as a dict - {"length":100, "total_words":15,
    "total_characters":85, "total_unique_words":12, "total_unique_characters":20}

2------is_english - takes a string as input and
 returns True if the text only contains English
  characters and return False if text contains at least
   one non-English character. ( Please use only python documentation.
    No other web resource should be used )
"""
import lab5.Class_liguist
print("enter your string with space at last")
string1=lab5.Class_liguist.Linguist(input())
print(string1.analyze_text())
print(string1.is_english())