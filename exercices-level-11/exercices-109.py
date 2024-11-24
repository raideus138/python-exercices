import random as r

palabras = {
    "Azuzaba": "Incitar",
    "Calamidad": "desgracia",
    "Contenciosas": "Conflictivo",
    "Despecho": "rencor",
    "Devastaba": "destrozar",
    "Dilaciones": "demora",
    "Engullir": "Devorar",
    "Etereo": "Sutil",
    "Exasperar": "Irritar",
    "Ignominia": "Deshonra",
    "Impetu": "Fuerza",
    "Impio": "cruel",
    "Incesante": "constante",
    "Indomito": "Salvaje",
    "Intransigente": "terco",
    "Lacerado": "Golpeado",
    "Lapidacion": "apedreamiento",
    "Merecimiento": "merito",
    "Montaraz": "Silvestre",
    "Perplejo": "asombrado",
    "Portentosas": "Maravilloso",
    "Prodigio": "Genio",
    "Proclama": "Declarar",
    "Propicio": "Favorable",
    "Transgredir": "violar",
    "Vanos": "Vacio",
    "Vastago": "descendiente",
    "Ventura": "Suerte",
}


usadas = set()

while True:
    if len(usadas) == len(palabras):
        print('Terminaste')
        break
    
    palabra = r.choice(list(set(palabras.keys()) - usadas))
    usadas.add(palabra)  

    user_value = input(f'Ingrese el sinonimo de "{palabra}": ')
    
    if user_value.lower() == palabras[palabra].lower():
        print('Has acertado')
    else:
        print(f'Te equivocaste, el sinónimo correcto era "{palabras[palabra]}". Intentalo de nuevo!')
