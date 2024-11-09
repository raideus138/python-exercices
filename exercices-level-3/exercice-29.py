'''Escribir un programa que pregunte al usuario la fecha de su 
nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
 Adaptar el programa anterior para que también funcione cuando
 el día o el mes se introduzcan con un solo carácter.'''

fecha = input('Introduzca su fecha de nacimiento e formato (dd/mm/aaaa): ')
fecha = fecha.split('/')
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
print(f'Naciste el dia {fecha[0]}, de {meses[int(fecha[1])-1]}, del {fecha[2]}')