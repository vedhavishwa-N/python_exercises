import random
class Astrologer (object):
    def __init__ (self,name):
        self.name = name
    global past, future



    past = ("in past life you were a robo-shark in the space",
      "in past life were a t-rex in modern world",
      "in past life you were a world serpent in norse mythology  ",
      "in past life you were a dog who travelled space",
      "in past life you were a commander in warzone",
      "this is your first life ")
    future = ("in the future you will become a billionare",
        "in the future you will be a rockstar",
        "in the future you will be a programmer")
    global memory_past, memory_future

    memory_past = {}
    memory_future = {}
    def get_past_life (self):
        name = self.name
        name = name.lower ()
        num = random.randint (0, 5)
        if name in memory_past:
            print (name, memory_past [name])

        else:
            print (name, past [num])
            memory_past [name] = past [num]

    def get_next_life (self):
        name = self.name
        name = name.lower ()
        num = random.randint (0, 2)
        if name in memory_future:
           print (name, memory_future [name])
        else:
            print (name, future [num])
            memory_future [name] = future [num]




