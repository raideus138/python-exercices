'''Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos 
en el último pedido y calcule el peso total del paquete que será enviado.'''
import math
Pp = 112
Pm = 75

iv = input('Cuantos payasos y muñecas se vendieron: ')
x = iv.split(" ")
payasos = int(x[0])
muñecas = int(x[1])
pt = ((payasos * 112)/1000) + ((muñecas * Pm)/1000)
print(f'El peso total del pedido es: {round(pt, 2)}kg')