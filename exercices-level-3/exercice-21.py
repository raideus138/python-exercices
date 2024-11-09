'''Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como 
el número introducido.'''

input = input('Ingrese su nombre y un numero: ')
n = input.split(',')
for i in range(int(n[1])):
    print(n[0])