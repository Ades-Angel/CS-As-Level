#Converts Denary to Binary

def denary_bin(a):
    '''This funtion converts denary numbers to binary.'''
    bin_value = []
    dividend = int(a)
    while True:
        reminder = dividend % 2
        quotient = dividend // 2
        bin_value.append(reminder)
        if quotient == 0:
            break
        dividend = quotient

    bin_value.reverse()
    return bin_value


denary_num = input('This is a denary to binary converter.Please enter a number: ')
print(str(denary_num) + ' in denary is: ' + str(denary_bin(denary_num)))
