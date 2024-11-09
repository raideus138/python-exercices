'''Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.'''
n = input('Ingrese sus horas trabajadas y su coste por hora separado por una coma: ')
n2 = n.split(",")
print(f'Tu paga es {int(n2[0]) * int(n2[1])}$')
