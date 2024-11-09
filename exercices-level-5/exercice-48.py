'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''
key = 2008
contraseña = 0
while contraseña != key:
    contraseña = int(input("Ingrese la contraseña: "))
    if contraseña != key:
        print('Contraseña incorrecta')
print('Acertaste')
