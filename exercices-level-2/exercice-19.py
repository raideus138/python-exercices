'''Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad
 de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y
  mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
 Redondear cada cantidad a dos decimales.'''

dinero = float(input('Ingrese el dinero de su cuenta de ahorro: '))
interes = 0.04

for i in range(1, 4):
    dinero = (dinero * interes) + dinero
    print(f'Despues del año numero {i} tendras {dinero}$')