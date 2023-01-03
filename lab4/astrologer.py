import random
past=("in past life you were a robo-shark in the space",
      "in past life were a t-rex in modern world",
      "in past life you were a world serpent in norse mythology  ",
      "in past life you were a dog who travelled space",
      "in past life you were a commander in warzone",
      "this is your first life ")
future=("in the future you will become a billionare",
        "in the future you will be a rockstar",
        "in the future you will be a programmer")
global memory
memory = {}

def get_past_life_v1(name):
    name=name.lower()
    num=random.randint(0,5)
    print(name,past[num])
    return

def get_past_life_v2(name):
    name = name.lower()
    num = random.randint(0, 5)
    if name in memory:
        print(name, memory[name])

    else:
        print(name, past[num])
        memory[name] = past[num]

def get_next_life(name):
    name = name.lower()
    num =random.randint(0,2)
    print(name,future[num])

