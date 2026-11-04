import time, os, sys
from input import choose
from colorama import Fore
debug = False

def typing(text):
   for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)
   value = input()  
   return value  

def chamber():
    print("After exploring the castle, you approach a door that towers over you." + Fore.RED + " You can feel an ominous presence inside..." + Fore.WHITE)
    enterChamber = choose(['y', 'n', 'rest'], "There's no time like the present...", "Enter? (y/n)\n> ")
    if enterChamber == "n":
        print("As you turn away from the door, you hear a roar as you look to your chest... ")
        time.sleep(2)
        print(Fore.RED + "...where blood now soaks your clothes..." + Fore.WHITE)
        print("GAME OVER.")
    elif enterChamber == "y":
        print("You push open the door...")
    elif enterChamber == "rest":
        print("You decide to rest for a second to gather your thoughts.")
        time.sleep(3)
        print(Fore.CYAN + "You open your eyes, your perception sharpened and determination burning." + Fore.WHITE)
        print("You push open the door...")
        debug = True
    else:
        print("Uh what happened here")
"""
Long have I slept amidst a endless dream...
Only to wake in this rotted world..
A world marred by plague, and death that I so disdain. 
Yet the flame of disdain I hold for this world is nothing but a ember...
...Compared to the roaring flame I feel towards you-
-the one who killed my brother. 
Now, feel my disdain.
"""


def dialogue(option):
    if option == 1:
        typing("A tall, armored figure lays across the marble floor.")
        typing("\"Long have I slept amidst a endless dream...\"")
        typing("Her voice roars.")
        typing("\"Only to wake in this rotted world..\"")
        typing("\"A world marred by plague, and death that I so disdain.\"")
        typing("The figure begins to push herself up off the floor.")
        typing("\"Yet the flame of disdain I hold for this world is nothing but a ember...\"")
        typing("\"...Compared to the roaring flame I feel towards you-\"")
        typing("You feel her bloodlust...")
        typing("\"-the one who killed my brother.\"")
        typing("A scepter appears in the armored figure's hand.")
        typing("\"Now...\"")
        typing("\"...feel my disdain.\"")

chamber()
dialogue(1)