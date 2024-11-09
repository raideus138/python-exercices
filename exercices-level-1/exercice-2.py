'''Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el
mayor de ellos. '''

def max_de_tres(a,b,c):
    if a > b:
        if a > c:
            return a
    if b > a:
        if b > c:
            return b
    if c > a:
        if c > b:
            return c

print(max_de_tres(2,12,5))