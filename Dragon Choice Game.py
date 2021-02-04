#Dragon Choice Game

import random  # Importing a file containing the random function.
import time


def displayIntro():  # def statement defines a new function. It has to have brackets and a colon (:) to define it. The def block must come before you call the funtion.
    print('''You are in a land full of dragons.In front of you, 
        you see two caves. In one cave, the dragon is friendly
        and will share his treasure with you. The other dragon
         is greedy and hungry, and will eat you on sight.''')


print()    # Three ''' allows you to have a string on several lines. Called multiline stirngs. 


def chooseCave():  # Use a while statement to ask a player to choose a cave. Which marks the start of a new kind of loop a "While loop". A while loop repeats as long as a certain condition is True. If it is False, then the while block is skipped.
    cave = ''  # Creates a variable called cave and stores a blank string in it. 
    while cave != '1' and cave != '2':  # Makes the player choose 1 or 2, nothing else. The loop here keeps asking which cave they choose until they enter a valid response. Called "input validation"
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave


def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2) #pauses the program for 2 sec in this case. Adds a pause.
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)  # Will randomly choose a number and either return 1 or 2.

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
