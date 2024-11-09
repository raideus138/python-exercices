'''Escribir un programa que guarde en una variable el
 diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al 
 usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.'''

d = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Ingrese una divisa: ")

if divisa.capitalize() in d:
    print(f'La divisa si está en el diccionario y su simbolo es {d[divisa.capitalize()]}')
else:
    print('La divisa no está en el diccionario')