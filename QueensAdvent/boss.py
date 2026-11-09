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

class Player:
    def __init__(self, health=100, debug=False):
        self.initHealth = health
        self.health = health
        self.choices = []
        self.describe = []
        self.initDecisions()
        self.initOutcomes()
        self.debug = debug

    def init(self):
        print("You")
        print(f"({self.health}) You ready your sword.")

    def initDecisions(self):
        self.choices += ["Attack", "Dodge", "Wait", "Defend", "Dodge and Attack", "Riposte", "Counterattack"]
        return self.choices

    def initOutcomes(self):
        self.describe += ["You swing your sword!", 
                            "You roll out of the way!", 
                            "You ready yourself...", 
                            "You raise your shield.", 
                            "You roll and jump into the air, swinging your blade down!", 
                            "You attack the fallen enemy, inflicting massive damage! (massive)", 
                            "After weaving, you counterattack!"]
        return self.describe

    def decideFrom(self, attackOptions):
        for i in range(len(attackOptions)):
            if attackOptions[i] in self.choices:
                print(f"[{i+1}] {attackOptions[i]}")
        choices = list(map(str, list(range(1,len(attackOptions)+1))))
        choice = int(choose(choices, "Try again.", "> ")) - 1 # translate into list form
        choiceName = attackOptions[choice]
        choiceIndex = self.choices.index(choiceName)
        print(self.describe[choiceIndex])
        return choiceName

    def decrHp(self, n):
        if self.health - n < 0: # Stops from going beyond 0
            self.health = 0
        else:
            self.health -= n
        print(f"You took {n} damage. (Health: {self.health})")
        return self.health

class Boss:
    def __init__(self, health, barLen, target):
        self.target = target
        self.initHealth = health
        self.health = health
        self.barLen = barLen
        self.stage = self.checkStage()
        self.attacks = self.initAttackDict()

    def init(self):
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
            taunts = ["The Queen scoffs at you.", "The Queen flips her hair.", "\"Don't make me laugh.\"", "\"I would have thought you smarter..\""]
            r = random.randint(0, len(taunts)-1)
            return taunts[r]

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

    def makeQTE(self, timing, text, key, damage=5):
        start = time.time()
        end = 0
        if input(f"{text} [{key.upper()} + ENTER] ").lower() == key:
            end = time.time()
            if (end - start) > timing: # failure
                outcome = -1
            else: # success
                outcome = 1
                print("Dodged!")
                damage = 0
        else:
            outcome = -1
        return [outcome, damage, None]      

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
                "text": "The Queen throws her spear!",
                "options": ["Attack", "Dodge", "Wait"],
                "goodOptions": ["Dodge"],
                "damage": 30,
                "id": 1,
            },{
                "name": "Short Blade Slice",
                "type": "active",
                "followUp": None,
                "text": "The Queen slashes her blade!",
                "options": ["Attack", "Dodge", "Wait"],
                "goodOptions": ["Dodge"],
                "damage": 10,
                "id": 2,
            }]
        return attacks

    def outcomeFromAttackChoice(self, id, choice):
        attack = self.attacks[id]
        damage = attack["damage"]
        if choice in attack["goodOptions"]:
            damage = 0
            outcome = -1
        else:
            outcome = 1
        return [outcome, damage, attack["followUp"]] # gives Queen if outcome is in her favor (1=yes, -1=not), damage she can inflict at this time, and if she can followUp (if outcome is in her favor AND she can followup, she will always followup.)

    def attack(self, id, canDodge=True):
        attack = self.attacks[id]
        print(attack["text"]) # Telegraph
        if not canDodge:
            print("You are staggered!")
            print(self.dialogue(3))
            return self.outcomeFromAttackChoice(id, -1)
        else:
            return self.outcomeFromAttackChoice(id, self.target.decideFrom(attack["options"])) # Returns a list with outcome

    def detNext(self, result):
        if result[1] != 0:
            self.target.decrHp(result[1])
        if result[2] != None:
            followUp = result[2]
            if result[0] != -1:
                self.detNext(self.attack(followUp["followUpAttackId"], False))
            else:
                R = random.random()
                if R < followUp["followUpChance"]:
                    self.detNext(self.attack(followUp["followUpAttackId"]))
                else:
                    print("The Queen falls, exhausted!")
        return 0

if chamber() != -1:
    You = Player()
    Queen = Boss(100, 20, You)
    # Queen.dialogue(1)
    Queen.init()
    You.init()
    print('...')
    Queen.detNext(Queen.makeQTE(1, "Dodge!", "d"))
    Queen.detNext(Queen.attack(0))