'''Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre
 posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo,
  y muestre por pantalla el grupo que le corresponde.'''

name = input("Como te llamas?: ")
gender = input("Cual es tu sexo (M o H)?: ")
if (gender == "M" and name.lower() < 'm') or (gender == "H" and name.lower() > 'n'):
    group = "A"
else:
    group = "B"
print("Tu grupo es " + group)