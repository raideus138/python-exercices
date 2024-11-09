'''Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.'''
def mcd(n, m):
    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n

def mcm(n, m):
    if n > m:
        g = n
    else:
        g = m
    while (g % n != 0) or (g % m != 0):
        g += 1
    return g

print(mcd(24,36))
print(mcm(24,36))