import time
import random

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
    time.sleep(3)
    
def chooseCave():
    cave=''
    while cave != "1" and cave != "2":
        print("Which cave will you go into? (1 or 2)")
        cave = input()
        
    return cave

def checkCave(chooseCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    time.sleep(2)
    
    rightCave = random.randint(1,2)
    
    if chooseCave == str(rightCave):
        print("Gives you the treasure!")
        time.sleep(2)

    else:
        print("Gobbles you down in one bite!")
        time.sleep(2)
        
playAgain = ""
while playAgain == "yes" or playAgain == "":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    playAgain = ""
    print()
    while playAgain != "yes" and playAgain != "no":
        print("You want to play again? (yes/no)")
        playAgain = str(input())
        playAgain = playAgain.lower()
        print()