'''Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience
 leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar 
 el precio habitual de una barra de pan,
 el descuento que se le hace por no ser fresca y el coste final total.'''
import random as r

precio_pan = 3.49
descuento = 0.6

panes_del_dia = r.randint(1,11)
panes_del_otro_dia = r.randint(1,11)

print(f'Usted lleva {panes_del_dia} panes del dia y {panes_del_otro_dia} panes que no son del dia, tiene un descuento de {panes_del_otro_dia * descuento}$ por llevar panes que no son del dia, el precio total es de {(panes_del_otro_dia * descuento) + panes_del_dia}')