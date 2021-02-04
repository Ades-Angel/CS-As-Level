#Logic Gate Simulation

def not_gate(a):
    if a == '1':
        return '0'
    else:
        return '1'


def and_gate(a, b):
    if a == '1' and b == '1':
        return '1'
    else:
        return '0'


def or_gate(a, b):
    if a == '0' and b == '0':
        return '0'
    else:
        return '1'


def nand_gate(a, b):
    if a == '1' and b == '1':
        return '0'
    else:
        return '1'


def nor_gate(a, b):
    if a == '0' and b == '0':
        return '1'
    else:
        return '0'


def xor_gate(a, b):
    if a == b:
        return '0'
    else:
        return '1'


while True:
    gate_choice = input('''This is a logic gate simulation. If you want:
1: Not gate 
2: And gate
3: Or gate
4: Nand gate
5: Nor gate
6: Xor gate
''')

    if gate_choice == '1':
        number_1 = input('Input: ')
        print('Not ' + number_1 + ' is: ' + not_gate(number_1))
    else:
        number_1 = input('Input 1: ')
        number_2 = input('Input 2: ')

        if gate_choice == '2':
            print(number_1 + ' And ' + number_2 + ' is: '+ and_gate(number_1, number_2))
        elif gate_choice == '3':
            print(number_1 + ' Or ' + number_2 + ' is: ' + or_gate(number_1, number_2))
        elif gate_choice == '4':
            print(number_1 + ' Nand ' + number_2 + ' is: ' + nand_gate(number_1, number_2))
        elif gate_choice == '5':
            print(number_1 + ' Nor ' + number_2 + ' is: ' + nor_gate(number_1, number_2))
        elif gate_choice == '6':
            print(number_1 + ' Xor ' + number_2 + ' is: ' + xor_gate(number_1, number_2))
        else:
            print('Invalid gate number.')
    # Ask user if they want simulation to run again
    again = input('Another simulation (y or n): ')
    if again == 'n' or again == 'N':
        break

