#Keypad

my_keypad = ['1 ', '2 ', '3'], ['4 ', '5 ', '6'], ['7 ', '8 ', '9'], ['* ', '0 ', '#']

print('This is your keypad:')
for row in my_keypad:
    keypad_row = ''
    for column in row:
        keypad_row += column
    print('[ ' + keypad_row + ' ]')
