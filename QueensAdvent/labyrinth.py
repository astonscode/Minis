from input import choose
import random

def generateSeed():
    a = random.randint(1,3)
    b = random.randint(1,3)
    c = random.randint(1,3)
    seed = str(a) + str(b) + str(c)
    return int(seed)

def labyrinth(seed=generateSeed()):
    # seed = 3 digits, either 1, 2, or 3. tells the correct path.
    parsedSeed = list(map(int, list(str(seed)))) # basically this takes the integer seed, makes it into a string so it can become a list, uses the map function to apply the int function to the entire array, all so we can split an int into a list lol
    mistakes = 0
    cYou = ""
    stuck = True
    startSpace = ""
    if parsedSeed[0] == 1:
        startSpace = "hallway"
    elif parsedSeed[0] == 2:
        startSpace = "door"
    elif parsedSeed[0] == 3:
        startSpace = "path"
    while stuck:
        for cPath in parsedSeed:
            if cPath == 1:
                print("You come to a set of three hallways. Which will you choose?")
                print("[1] Go down the left corridor.\n[2] Go down the middle corridor.\n[3] Go down the right corridor.")
                cYou = choose(["1", "2", "3"], "You stumble around confused. Try again?", "> ")
            elif cPath == 2:
                print("You come to a set of three doors. Which will you choose?")
                print("[1] The left door.\n[2] The middle door.\n[3] The right door.")
                cYou = choose(["1", "2", "3"], "You stumble around confused. Try again?", "> ")
            else:
                print("You come to a set of three paths. Which will you choose?")
                print("[1] Travel left.\n[2] Travel straight.\n[3] Travel right.")
                cYou = choose(["1", "2", "3"], "You stumble around confused. Try again?", "> ")
            if cPath != int(cYou):
                print("This path was longer than the previous one.")
                mistakes += 1
        if mistakes > 0:
            print(f"These {startSpace}s look familiar... must be your imagination.")
            mistakes = 0
        else:
            stuck = False
            print("...")
    print("You arrive at an exit to the labrynth.")
    print("You escaped...")
    return parsedSeed

labyrinth()