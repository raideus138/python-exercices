'''Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla 
el capital obtenido en la inversión.'''

n = input('Que cantidad desea invertir, el interes anual y a cuantos años: ')
n = n.split(' ')
print(f'Al pasar {int(n[2])} años, sus {int(n[0])}$ invertidos se convertiran en {(int(n[0]) * (float(n[1])/100) * int(n[2])) + int(n[0])}')

