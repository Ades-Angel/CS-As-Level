#Age Check 

myAge = int(input('What is your age: '))

if myAge < 0 or myAge > 100:
    print('Are you a wizard!')
elif myAge < 12:
    print('Your are a child. Cute!')
elif myAge < 18:
    print('Your are a teenager. Awesome!')
else:
    print('Your are an adult! Cool!')
