import random
import time
import os

draws = 0
computer_wins = 0
player_wins = 0
player_lives = 10
computer_lives = 10


def start_menu():
    '''Welcomes player, defines the menu action and executes them.'''
    print('Welcome to Rock, Paper and Scissors.')
    time.sleep(0.5)
    print("To see the rules of the game enter 'Rules'.")
    time.sleep(0.5)
    print("To start the game enter 'Play'.")
    user_choice = input()


def see_rules():
    print('Rules:')
    print('-Paper beats Rock.')
    print('-Rock beats Scissors.')
    print('-Scissors beats Paper.')
    print('You start with 10 lives.')
    print('The computer start with 10 lives.')
    print('We will keep score of how many times you and the computer won.')
    print('But also how many times you drew.')
    print('Try to beat the computer.Good Luck!')


def player_weapon():
    '''Gets the player to choose a weapon.'''
    player_choice = input('Choose Rock (R), Paper(P) or Scissors(S): ')
    if player_choice in ['Rock', 'rock', 'r', 'R']:
        player_choice = 'Rock'
    elif player_choice in ['Paper', 'paper', 'p', 'P']:
        player_choice = 'Paper'
    elif player_choice in ['Scissors', 'scissors', 's', 'S']:
        player_choice = 'Scissors'
    elif player_choice in ['Exit', 'exit', 'E', 'e']:
        player_choice = 'e'
    else:
        print('')
        print("I don't understand, try again.")
    return player_choice


def computer_weapon():
    '''Randomly chooses the computer's weapon.'''
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice = 'Rock'
    elif computer_choice == 2:
        computer_choice = 'Paper'
    else:
        computer_choice = 'Scissors'
    return computer_choice


def find_winner():
    '''Finds who won the match and keeps track of lives and wins.'''
    draws = 0
    computer_wins = 0
    player_wins = 0
    player_lives = 10
    computer_lives = 10 
    if player == computer:
        print('')
        time.sleep(0.5)
        print('You chose',player)
        print('')
        time.sleep(0.5)
        print('The computer chose',computer)
        print('')
        time.sleep(0.5)
        print('You drew')
        time.sleep(0.5)
        draws += 1 
        print('')
        print('You drew', draws, 'times')
        print('Computer has won', computer_wins, 'times')
        print('You won', player_wins, 'times')
        print('The computer has', computer_lives, 'lives left')
        print('You have', player_lives, 'lives left')
        draws += 1 
    elif player == 'Rock':
        if computer == 'Paper':
            print('')
            time.sleep(0.5)
            print('You chose',player)
            print('')
            time.sleep(0.5)
            print('The computer chose',computer)
            print('')
            time.sleep(0.5)
            print('You lost. The computer beat you.')
            time.sleep(0.5)
            computer_wins += 1 
            player_lives -= 1
            print('')
            print('You drew', draws, 'times')
            print('Computer has won', computer_wins, 'times')
            print('You won', player_wins, 'times')
            print('The computer has', computer_lives, 'lives left')
            print('You have', player_lives, 'lives left')
        elif computer == 'Scissors':
            print('')
            time.sleep(0.5)
            print('You chose',player)
            print('')
            time.sleep(0.5)
            print('The computer chose',computer)
            print('')
            time.sleep(0.5)
            print('You won! You beat the computer.')
            time.sleep(0.5)
            player_wins += 1 
            computer_lives -= 1
            print('')
            print('You drew', draws, 'times')
            print('Computer has won', computer_wins, 'times')
            print('You won', player_wins, 'times')
            print('The computer has', computer_lives, 'lives left')
            print('You have', player_lives, 'lives left')
    elif player == 'Paper':
        if computer == 'Scissors':
            print('')
            time.sleep(0.5)
            print('You chose',player)
            print('')
            time.sleep(0.5)
            print('The computer chose',computer)
            print('')
            time.sleep(0.5)
            print('You lost. The computer beat you.')
            time.sleep(0.5)
            computer_wins += 1 
            player_lives -= 1
            print('')
            print('You drew', draws, 'times')
            print('Computer has won', computer_wins, 'times')
            print('You won', player_wins, 'times')
            print('The computer has', computer_lives, 'lives left')
            print('You have', player_lives, 'lives left')
        elif computer == 'Rock':
            print('')
            time.sleep(0.5)
            print('You chose',player)
            print('')
            time.sleep(0.5)
            print('The computer chose',computer)
            print('')
            time.sleep(0.5)
            print('You won! You beat the computer.')
            time.sleep(0.5)
            player_wins += 1 
            computer_lives -= 1
            print('')
            print('You drew', draws, 'times')
            print('Computer has won', computer_wins, 'times')
            print('You won', player_wins, 'times')
            print('The computer has', computer_lives, 'lives left')
            print('You have', player_lives, 'lives left')
    elif player == 'Scissors':
        if computer == 'Rock':
            print('')
            time.sleep(0.5)
            print('You chose',player)
            print('')
            time.sleep(0.5)
            print('The computer chose',computer)
            print('')
            time.sleep(0.5)
            print('You lost. The computer beat you.')
            time.sleep(0.5)
            computer_wins += 1 
            player_lives -= 1
            print('')
            print('You drew', draws, 'times')
            print('Computer has won', computer_wins, 'times')
            print('You won', player_wins, 'times')
            print('The computer has', computer_lives, 'lives left')
            print('You have', player_lives, 'lives left')
        elif computer == 'Paper':
            print('')
            time.sleep(0.5)
            print('You chose',player)
            print('')
            time.sleep(0.5)
            print('The computer chose',computer)
            print('')
            time.sleep(0.5)
            print('You won! You beat the computer.')
            time.sleep(0.5)
            player_wins += 1 
            computer_lives -= 1
            print('')
            print('You drew', draws, 'times')
            print('Computer has won', computer_wins, 'times')
            print('You won', player_wins, 'times')
            print('The computer has', computer_lives, 'lives left')
            print('You have', player_lives, 'lives left')


user_choice = start_menu()
if user_choice == 'Rules':
    see_rules()
    start_menu()
if user_choice == 'Play':
    while True:
        print('')
        player = player_weapon()
        computer = computer_weapon()
        find_winner()
        if user_choice == 'e':
            break