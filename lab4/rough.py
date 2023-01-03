"""global memory
memory = {}
import astrologer

for num in range(0, 3):
    print("enter your name: ")
    name = input()
    print(astrologer.get_past_life_v1(name, memory))
    print(astrologer.get_past_life_v2(name, memory))
    memory[name] = astrologer.l[num]
    print(memory)

    already_existing_astro = {}
    name - key, value - asgo
    content
    next = yes
    while next == yes:
        name = input()
        if name in already_existing_astro:
            print(already_existing_astro[name])
        else:
            astro = get_astro(name)
            already_existing_astro[name] = astro
        next = input(): print("yes- continue \ other exit")

"""