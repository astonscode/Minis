# Run tests ( > 5) still experimental, needs calibration and review from players

# Issues

# 1. AI Level does not display properly in datatext 
# Solution: Create a function that returns the value as the level's name instead of its value 

# 2. Sometimes, the AI will use Action 2 (Shooting itself) and its turn will end. This may be just a missed return or non-escaped string. 
# Solution: i dunno you own your own for this one

# 3. 'cause' variable does not update on save. It throws 'variable not accessed, but its literally not in anything, so its weird i guess
# Solution: declaring it global in the function may fix it

import random
import time
import datetime
import sys

game = True
debug = True
intro = False

bullet = 0
barrel = 0
willShoot = bullet == barrel
cause = 0 

turn = 0
turns = 0

gameWon = 0

aiLevel = 0

loop = True

def debug_print(s):
    if debug:
        print(f"\n[DEBUG] {s}")

def useGun(player, action): # to be removed
    global cause
    if player == 1:
        if action == 1:
            if barrel == bullet:
                print("\nYou successfully shot your opponent.")
                cause = "Successful Prediction"
                return 1
            elif barrel != bullet:
                print("\nThe gun didn't fire.")
                return 0
            else:
                print("\nSomething went wrong.")
                exit()
        elif action == 2:
            if barrel == bullet:
                print("\nYou shot yourself...")
                cause = "Suicide"
                return 1
            elif barrel != bullet:
                print("\nThe gun didn't fire.")
                return 0
            else:
                print("\nSomething went wrong.")
                exit()
    elif player == 2:
        if action == 1:
            if barrel == bullet or barrel < 0:
                print("\nAI chose: \t[1]")
                time.sleep(3)
                print("\nYou were shot by your opponent.")
                cause = "Death"
                return 1
            elif barrel != bullet:
                print("\nAI chose: \t[1]")
                time.sleep(3)
                print("\nThe gun didn't fire.")
                return 0
            else:
                print("\nSomething went wrong.")
                exit()
        elif action == 2:
            if barrel == bullet:
                print("\nAI chose: \t[2]")
                time.sleep(3)
                print("\nThe AI shot itself.")
                cause = "Suicide"
                return 1
            elif barrel != bullet:
                print("\nAI chose: \t[2]")
                time.sleep(3)
                print("\nThe gun didn't fire.")
                return 0
            else:
                print("\nSomething went wrong.")
                exit()
    else:
        print("uhhhh...")

def save():
    with open("cnry_data.txt", "a") as file:
        name = input("Enter your name:\t")
        timestamp = datetime.datetime.now()
        if gameWon:
            result = "WIN"
        else: 
            result = "LOSS"

        if aiLevel == 1:
            ai = "Normal"
        elif aiLevel == 5:
            ai = "Extreme"
        else:
            ai = "AI"

        file.write(f"[{timestamp.strftime("%a %b %d, %H:%M:%S")}] {str(name)} {result} vs {ai} by {cause} (Turns: {turns})\n")
        print("Saved!")

def choose():
    l = True
    while l:
        try:
            bullet = random.randint(0, 6)
            barrel = random.randint(0, 6)
            willShoot = bullet == barrel
            debug_print(f"bullet: {bullet}, barrel: {barrel}, willShoot: {willShoot}")
            print("\nWhat would you like to do?")
            
            print("\n[1]\tShoot Opponent")
            print("\tShooting your opponent will end your turn if a bullet does not fire.")

            print("\n[2]\tShoot Yourself")
            print("\tShooting yourself will skip the opponents turn.")

            choice = int(input("\n[1/2] "))

            if choice < 1 or choice > 2:
                raise ValueError("Please choose an option.")
        except ValueError:
            print("Try again.")
        else:
            l = False
    return choice

def shoot(chose, player):
    if willShoot and chose == 2:
        if player == 0:
            print("\nYou shot yourself...")
        elif player == -1:
            print("\nThe AI shot itself...")
        elif player >= 1:
            print(f"\nPlayer {player} shot theirself...")
        else:
            print("Something went wrong.")
    elif willShoot and chose == 1:
        if player == 0:
            print("\nYou shot your opponent.")
        elif player != 0:
            print("\nThe gun fired...")
        else:
            print("Something went wrong.")
    else:
        print("\nThe gun didn't fire.")

while True:
    shoot(choose(), 0)

sys.exit(0)

class AI:
    def __init__(self, difficulty=None):
        if difficulty is None:
            difficulty()
        else:
            self.difficulty = difficulty
        self.isActive = False

    def difficulty(self):
        l = True
        while l:
            try:
                choice = input("Set AI Difficulty [Normal / Extreme]:\t")
                if choice.lower() == "normal":
                    print("\nSetting AI difficulty to Normal. ")
                    self.difficulty = 1
                elif choice.lower() == "extreme":
                    print("\nSetting AI difficulty to Extreme.")
                    self.difficulty = 5
                else:
                    l = True
            except ValueError:
                print("Try again.")
                l = True

    def chooseAction(self):
        if self.difficulty == 1:
            self.normal()
        elif self.difficulty == 5:
            self.extreme()
        else:
            print("Something went wrong.")

    def normal(self):
        r = random.randint(1,2)
        print(f"AI chose [{r}]...")
        time.sleep(2)

    def extreme(self):
        ...
                
if intro == True: # to be removed
    print("-- A game by Aston and Brandon -- ")
    time.sleep(3)
    print("\nExperiment no. 2: roulette")
    time.sleep(4)
    print("h a v e  f u n . ")

while loop == True: # to be removed

    while game == True:
        turns += 1

        print(f"Turn {turns}: P1")

        debug_print(f"bullet: {bullet}; barrel: {barrel};")

        while turn == 0:
            print("\nWhat would you like to do?")

            print("\n[1]\tShoot Opponent")
            print("\tShooting your opponent will end your turn if a bullet does not fire.")

            print("\n[2]\tShoot Yourself")
            print("\tShooting yourself will skip the opponents turn.")

            choice = int(input("\n[1/2]\t"))

            debug_print(f"choice: {choice}")

            if choice == 1:
                if barrel <= 0:
                    barrel = 6 

                a = useGun(1, 1)

                barrel -= 1

                if a == 1:
                    gameWon = True
                    game = False
                    break
                elif a == 0:
                    turn = 1
                    turns += 1

                debug_print(f"bullet: {bullet}; barrel: {barrel};")
                
            elif choice == 2:
                if barrel <= 0:
                    barrel = 6

                a = useGun(1, 2)
                
                barrel -= 1

                if a == 1:
                    gameWon = False
                    game = False
                    break 
                elif a == 0:
                    turn = 0
                    turns += 1

                debug_print(f"bullet: {bullet}; barrel: {barrel};")
                
                
        while turn == 1:
            print("\nAI's Turn:")

            debug_print(f"bullet: {bullet}; barrel: {barrel}; aiLevel : {aiLevel}")

            print("AI is thinking...")

            time.sleep(3)

            if aiLevel == 5:
                if bullet + 1 == barrel or bullet - 1 == barrel or barrel == 0:
                    if barrel <= 0:
                        barrel = 6 

                    a = useGun(2, 1)

                    barrel -= 1

                    if a == 1:
                        gameWon = False
                        game = False
                        break
                    elif a == 0:
                        turn = 0
                        turns += 1

                    debug_print(f"bullet: {bullet}; barrel: {barrel};")
                elif bullet + 2 == barrel or bullet - 2 == barrel:
                    if barrel <= 0:
                        barrel = 6 

                    a = useGun(2, 2)

                    barrel -= 1

                    if a == 1:
                        gameWon = True
                        game = False
                        break 
                    elif a == 0:
                        turn = 1
                        turns += 1

                    debug_print(f"bullet: {bullet}; barrel: {barrel};")
                else:
                    if barrel <= 0:
                        barrel = 6 
                    
                    a = useGun(2, 2)

                    barrel -= 1

                    if a == 1:
                        gameWon = True
                        game = False
                        break 
                    elif a == 0:
                        turn = 0
                        turns += 1

                    debug_print(f"bullet: {bullet}; barrel: {barrel};")
            elif aiLevel == 1:
                if barrel <= 0:
                    barrel = 6 

                i = random.randint(1, 2)

                if i == 1:
                    a = useGun(2, 1)
                    if a == 1:
                        gameWon = False
                        game = False
                        break 
                    elif a == 0:
                        turn = 0
                        turns += 1
                        barrel -= 1
                elif i == 2:
                    a = useGun(2, 2)
                    if a == 1:
                        gameWon = True
                        game = False
                        break 
                    elif a == 0:
                        turn = 1
                        turns += 1
                        barrel -= 1

    if gameWon == True:
        print("\nCongratulations! You won!")
        choice = input("\nSave your score? (y/n)\t")
        if choice == "y":
            save()
    elif gameWon == False:
        print("\nYou lost...")
        choice = input("\nSave your score? (y/n)\t")
        if choice == "y":
            save()

    b = input("\033[31ma g a i n ? (y/n)\033[0m\t")

    if b == "y":
        loop = True

        game = True
        debug = False

        bullet = random.randint(0, 6)
        barrel = random.randint(0, 6)

        turn = 0
        turns = 0

        gameWon = 0
    elif b == "n":
        print("\033[31ms e e  y o u . . .\033[0m")
        loop = False