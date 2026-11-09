import time, sys, random
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
        return -1
    elif enterChamber == "y":
        print("You push open the door...")
        return 1
    elif enterChamber == "rest":
        print("You decide to rest for a second to gather your thoughts.")
        time.sleep(3)
        print(Fore.CYAN + "You open your eyes, your perception sharpened and determination burning." + Fore.WHITE)
        print("You push open the door...")
        debug = True
        return 1
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

class Queen:
    def __init__(self, health, barLen):
        self.initHealth = health
        self.health = health
        self.barLen = barLen
        self.stage = self.checkStage()
        self.attacks = self.initAttackDict()

    def initialize(self):
        print("The Queen")
        print(self.genHealthbar())
        print(f"({self.health}) {self.dialogue(2)}")

    def dialogue(self, line):
        if line == 1: # ONLY USE OUTSIDE OF F-STRINGS
            typing("A tall, armored figure lays across the marble floor.")
            typing("\"Long have I slept amidst an endless dream...\"")
            typing("She breathes.")
            typing("\"Only to wake in this rotted world..\"")
            typing("\"A world marred by plague, and death that I so disdain.\"")
            typing("The figure begins to push herself from the floor.")
            typing("\"Yet the flame of disdain I hold for this world is nothing but an ember...\"")
            typing("\"...Compared to the roaring flame I feel towards you-\"")
            typing("You feel her bloodlust...")
            typing("\"-the one who killed my brother.\"")
            typing("A scepter appears in the armored figure's hand.")
            typing("\"Now...\"")
            typing("\"...feel my disdain.\"")
        elif line == 2:
            return "The Queen advances towards you."
        elif line == 3:
            return "The Queen scoffs at you."

    def checkStage(self):
        if self.health <= round(self.initHealth / 2):
            stage = 2
        else:
            stage = 1
        return stage

    def genHealthbar(self):
        remaining = self.health / self.initHealth
        hp = 0
        healthBar = "["
        for _ in range(round(self.barLen * remaining)):
            healthBar += "|"
            hp += 1
        if hp < self.barLen:
            for _ in range(self.barLen - hp):
                healthBar += "."
        healthBar += "]"
        return healthBar

    def decrHp(self, n):
        if self.health - n < 0: # Stops from going beyond 0
            self.health = 0
        else:
            self.health -= n
        self.stage = self.checkStage()
        return self.health

    def incrHp(self, n):
        if self.health + n > self.initHealth: # Stops from going above max
            self.health = self.initHealth
        else:
            self.health += n
        return self.health

    def makeQTE(self, timing, text, key):
        start = time.time()
        end = 0
        if input(f"{text} [{key.upper()}] ").lower() == key:
            end = time.time()
            if (end - start) > timing:
                outcome = -1
            else:
                outcome = 1
        else:
            outcome = -1
        return outcome      

    def initAttackDict(self):
        attacks = [{
                "name": "Spear Throw (Prepare)",
                "type": "prepare",
                "followUp": {
                    "canFollowUp": True,
                    "followUpChance": 1,
                    "followUpAttackId": 1,
                },
                "text": "The Queen raises her spear...",
                "options": ["Attack", "Dodge", "Wait"],
                "goodOptions": ["Wait"],
                "damage": 0, 
                "id": 0,
            },{
                "name": "Spear Throw (Active)",
                "type": "active",
                "followUp": {
                    "canFollowUp": True,
                    "followUpChance": 0.5,
                    "followUpAttackId": 2,
                },
                "text": "The Queen throws her spear",
                "damage": 30,
                "id": 1,
            },{
                "name": "Short Blade Slice",
                "type": "active",
                "followUp": None,
                "text": "The Queen slashes her blade",
                "damage": 10,
                "id": 2,
            }]
        return attacks

    def outcomeFromAttackChoice(self, id, choice):
        attack = self.attacks[id]
        c = attack["options"][int(choice) - 1]
        if c in attack["goodOptions"]:
            print(f"{c} Good")
            return 1
        else:
            print(f"{c} Bad")
            return -1

    def attack(self, id):
        attack = self.attacks[id]
        print(attack["text"]) # Telegraph
        print("What do you want to do?") # Ask for choice
        options = attack["options"]
        for i in range(len(options)):
            print(f"[{i+1}] {options[i]}")
        choices = map(str, list(range(1,4)))
        choice = choose(list(choices), "Try again.", "> ")
        return self.outcomeFromAttackChoice(id, choice)

if chamber() != -1:
    Boss = Queen(100, 20)
    # Boss.dialogue(1)
    Boss.initialize()
    # if Boss.makeQTE(1, "Dodge!", "d") == -1: print("-20")
    Boss.attack(0)
    


