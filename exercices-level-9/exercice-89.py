'''Escribir una función reciba una lista de notas y devuelva 
la lista de calificaciones correspondientes a esas notas. '''

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
    return list(map(grade, scores))

print(apply_grade([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10]))