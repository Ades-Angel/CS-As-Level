#Lists

list = []
odd_list = []
even_list = []
list_length = int(input('How many numbers do you want to enter? ' ))

for i in range(list_length):
    numbers = int(input('Enter your numbers: '))
    list.append(numbers)

for num in list:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print('Even numbers: ' + str(even_list))
print('Odd numbers: ' + str(odd_list))
