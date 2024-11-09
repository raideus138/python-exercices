'''Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
 separados por comas, y muestre por pantalla
 cada uno de los productos en una línea distinta.'''
productos = input('Ingrese todos los productos de su lista de comrpas separados por una coma: ')
productos = productos.split(",")
for producto in productos:
    print(producto)