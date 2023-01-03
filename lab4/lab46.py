"""Create a module called "astrologer".
 It should have a function called get_past_life which
  should take the name of a person as an argument
  and give a random description of the past life of
   the person as the return value. Keep a decent number
    of past life descriptions ( 5 ). The descriptions
    could be "You were a mathematician in your past life",
 "You were a horse in your past life" etc."""
import astrologer
print("enter your name: ")
name = input()
name.lower()
print(astrologer.get_past_life_v1(name))

