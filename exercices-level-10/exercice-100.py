'''El fichero calificaciones.csv contiene las calificaciones de un curso.
 Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. 
 Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en la al 
 final del curso (convocatoria ordinaria). Escribir un programa que contenga las siguientes funciones:

-Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios,
 donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. 
 La lista tiene que estar ordenada por apellidos.

-Una función que reciba una lista de diccionarios como la que devuelve la función anterior y 
añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de 
teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.

-Una función que reciba una lista de diccionarios como la que devuelve la función anterior y
 devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. 
 Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes parciales
  y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.'''

def nota(cifra):
    cifra = cifra.replace(',','.')
    return float(cifra) 

def calificaciones(ruta):

    try:
        f = open(ruta, 'r')
    except FileNotFoundError:
        print('El fichero no existe.')
        return
    lineas = f.readlines()
    f.close()
    claves = lineas[0][:-1].split(";")
    calificaciones = []
    for i in lineas[1:]:
        valores = i[:-1].split(";")
        alumno = {}
        for j in range(len(valores)):
            alumno[claves[j]] = valores[j]
        calificaciones.append(alumno)
    return calificaciones

def añadir_nota_final(calificaciones):


    def nota_final(alumno):

        if alumno['Ordinario1']: 
            parcial1 = nota(alumno['Ordinario1'])
        elif alumno['Parcial1']:
            parcial1 = nota(alumno['Parcial1'])
        else: 
            parcial1 = 0
        if alumno['Ordinario2']:
            parcial2 = nota(alumno['Ordinario2'])
        elif alumno['Parcial2']:
            parcial2 = nota(alumno['Parcial2'])
        else: 
            parcial2 = 0 
        if alumno['OrdinarioPracticas']: 
            practicas = nota(alumno['OrdinarioPracticas'])
        elif alumno['Practicas']:
            practicas = nota(alumno['Practicas'])
        else:
            practicas = 0
        alumno['Final1'] = parcial1
        alumno['Final2'] = parcial2
        alumno['FinalPracticas'] = practicas
        alumno['NotaFinal'] = parcial1 * 0.3 + parcial2 * 0.3 + practicas * 0.4
        return alumno

    return list(map(nota_final, calificaciones))

def aprobados_suspensos(calificaciones):
    aprobados = []
    suspensos = []
    for alumno in calificaciones:
        if all([int(alumno['Asistencia'][:-1]) >= 75, alumno['Final1'] >= 4, alumno['Final2'] >=4, alumno['FinalPracticas'] >=4, alumno['NotaFinal'] >= 5]):
            aprobados.append(alumno['Apellidos'] + ', ' + alumno['Nombre'])
        else:
            suspensos.append(alumno['Apellidos'] + ', ' + alumno['Nombre'])
    return aprobados, suspensos

print(añadir_nota_final(calificaciones('calificaciones.csv')))
aprobados, suspensos = aprobados_suspensos(añadir_nota_final(calificaciones('calificaciones.csv')))
print('Lista de aprobados:', aprobados)
print('Lista de suspensos:', suspensos)
