'''
Generate a random Password which meets the following conditions
    -Password length must be 10 characters long.
    -It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

'''
import string as s
import random as r
lenght = 10
chars = s.printable
uppercase = s.ascii_uppercase
digits = s.digits
symbols = s.punctuation
word = ''
for i in range(1,lenght+1):
    for j in range(1,3):
        word += r.choice(uppercase)
    for k in range(1,2):
        word += r.choice(symbols)
    word += r.choice(chars)
    
print(len(word))