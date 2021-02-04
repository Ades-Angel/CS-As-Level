#ISBN Check

def check_valid_isbn(isbn):
    check_digit = int(isbn[12])
    even_sum = int(isbn[0]) + int(isbn[2]) + int(isbn[4]) + int(isbn[6])
    + int(isbn[8]) + int(isbn[10])
    odd_sum = int(isbn[1]) * 3 + int(isbn[3]) * 3 + int(isbn[5]) * 3
    + int(isbn[7]) * 3 + int(isbn[9]) * 3 + int(isbn[11]) * 3
    total_sum = even_sum + odd_sum
    isbn_check = 10 - (total_sum % 10)
    if isbn_check == check_digit:
        print('Your ISBN number is correct.')
    else:
        print('Your ISBN number is incorrect.')


isbn = input('Please enter an ISBN number: ')
while len(isbn) != 13:
    isbn = input('Please enter a 13 digit ISBN number: ')


check_valid_isbn(isbn)
