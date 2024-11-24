'''
Realizar un programa que pregunte al usuario por un número entero impar 
y dibuje un rombo con el número de filas introducidas por el usuario.
'''

n = int(input('Ingrese un numero impar: '))

if n % 2 == 0:
    n += 1

x = '*'

for j in range(1,n+1, 2):
    print("{:^33}".format(j * x))
for k in range(n-2, 1, -2):
    print("{:^33}".format(k * x))
print("{:^33}".format('*'))
