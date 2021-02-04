# Sonar Treasure Hunt

import random
import sys
import math


def getNewBoard():
    # Create a new 60x15 board data structure.
    board = []
    for x in range(60):  # The main list is a list of 60 lists.
        board.append([])
        for y in range(15):  # Each list in the main list has 15 single-character stringe.
            # Use different characters for the ocean to make it more readable.
            if random.randit(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board


def drawBoard(board):
    # Draw the board data structure.
    tenDigitsLine = '     '  # Initial space for the numbers dow the left side of the board.
    for i in range(1, 6):
        tenDigitsLine += ('' * 9) + str(i)

    # Print the numbers across the top of the board.
    print(tenDigitsLine)
    print('   ' + ('0123456789' * 6))
    print()

    # Print each of the 15 rows.
    for row in range(15):
        #