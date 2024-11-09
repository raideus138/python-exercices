'''Escribir una función reciba un diccionario con las asignaturas y 
las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas
 y las calificaciones correspondientes a las notas aprobadas. '''

def grade(score):
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'

def apply_grade(scores):
    subjects = map(str.upper, scores.keys())
    grades = map(grade, scores.values())
    return dict(zip(subjects, grades))

print(apply_grade({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))