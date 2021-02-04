#Money Converter

print('''This is a converter. If you want to convert
1. Euros to Us dollars or vise versa
2. Euros to Thai baht or vise versa
3. Us dollars to Thai baht or vise versa
Enter 1, 2, or 3: ''')
answer = int(input())

if answer == 1:
    print('''Enter to change from
    1. Euros to Us dollars.
    2. Us dollars to Euros.''')
    choice = int(input())
    number = int(input('Enter the amount you want to convert: '))
    if choice == 1:
        rate = 1.11
        convertion = round((rate * number), 2)
        print(str(number) + ' Euros in Us dollars is: ' + str(convertion))
    else:
        rate = 0.90
        convertion = round((rate * number), 2)
        print(str(number) + ' Us dollars in Euros is: ' + str(convertion))

if answer == 2:
    print('''Enter to change from
    1. Euros to Thai baht.
    2. Thai baht to Euros.''')
    choice = int(input())
    number = int(input('Enter the amount you want to convert: '))
    if choice == 1:
        rate = 33.60
        convertion = round((rate * number), 2)
        print(str(number) + ' Euros in Thai baht is: ' + str(convertion))
    else:
        rate = 0.030
        convertion = round((rate * number), 2)
        print(str(number) + ' Thai baht in Euros is: ' + str(convertion))

if answer == 3:
    print('''Enter to change from
    1. Us dollars to Thai baht.
    2. Thai baht to Us dollars.''')
    choice = int(input())
    number = int(input('Enter the amount you want to convert: '))
    if choice == 1:
        rate = 0.033
        convertion = round((rate * number), 2)
        print(str(number) + ' Us dollars in Thai baht is: ' + str(convertion))
    else:
        rate = 30.23
        convertion = round((rate * number), 2)
        print(str(number) + ' Thai baht in Us dollars is: ' + str(convertion))
 