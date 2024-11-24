'''Generate random String of length 5'''
import string as s
import random as r

chars = s.ascii_lowercase
word = ''
for i in range(1,6):
    word += r.choice(chars)
print(word)