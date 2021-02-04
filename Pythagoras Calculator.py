#Pythagoras Calculator

import math

print('''This is a Pythagoras calculator. Enter the side you want to calculate.
a for Adjacent
o for Opposite
h for Hypotenuse''')
answer = str(input())

while True:
    if answer == 'a' or answer == 'o' or answer == 'h':
        break
    else:
        answer = input('Please enter a,o or h: ')

if answer == 'a':
    o = int(input('Enter a number for o: '))
    h = int(input('Enter a number for h: '))
    a_answer = round((math.sqrt(h * h - o * o)), 2)
    print(a_answer)
elif answer == 'o':
    a = int(input('Enter a number for a: '))
    h = int(input('Enter a number for h: '))
    o_answer = round((math.sqrt(h * h - a * a)), 2)
    print(o_answer)
else:
    a = int(input('Enter a number for a: '))
    o = int(input('Enter a number for o: '))
    h_answer = round((math.sqrt(a * a + o * o)), 2)
    print(h_answer)
