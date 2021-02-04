# Encryption

def encryption(word, key):
    ''' This is a Caesar Cypher. Please enter a word and a key.
        The function loops through the characters and find its new letter.
        Then it returns the encrypted word.  '''
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_word = ''
    for char in word:
        if char in lower_alphabet:
            lower_location = lower_alphabet.find(char)
            lower_new_location = (lower_location + key) % 26
            lower_new_letter = lower_alphabet[lower_new_location]
            encrypted_word += lower_new_letter
        if char in upper_alphabet:
            upper_location = upper_alphabet.find(char)
            upper_new_location = (upper_location + key) % 26
            upper_new_letter = upper_alphabet[upper_new_location]
            encrypted_word += upper_new_letter
    return encrypted_word


print('This is a Caesar Cypher. ')
word = input('Enter the word to be encrypted/decrypted: ')
key = int(input('Please enter a key (encrypt) or a negative key (decrypt): '))
encrypted_word = encryption(word, key)
print(encrypted_word)
