#Gives Name in ASCII, Hexadecimal and Binary

print('''This program will give your name in ASCII then in Hexadecimal
and Bianry.''')
name = input('Please enter your name: ')
print('Char    ' + 'ASCII    ' + 'Hex     ' + 'Binary  ')

for char in name:
    ascii_value = ord(char)
    hexadecimal = hex(ascii_value)
    binary = bin(ascii_value)
    print(char, '\t', ascii_value, '\t', hexadecimal[2:], '\t', binary[2:])
