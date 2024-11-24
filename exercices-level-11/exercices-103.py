'''
Escriba un programa que obtenga el máximo y el mínimo de una serie de datos proporcionados en Hexadecimal.
Para ello se le pasará una lista de datos en formato hexadecimal, y tendrá que convertirlos primero a formato Binario, 
y a continuación a formato Decimal.
'''

def conversion_hex_bin(num_hex):
    hexbin = {
            "0":"0000",
            "1":"0001", 
            "2":"0010", 
            "3":"0011", 
            "4":"0100", 
            "5":"0101", 
            "6":"0110", 
            "7":"0111", 
            "8":"1000", 
            "9":"1001", 
            "A":"1010", 
            "B":"1011", 
            "C":"1100",
            "D":"1101", 
            "E":"1110", 
            "F":"1111"}
    num_bin = "" 
    for i in num_hex: 
        try:
            num_bin += hexbin[i]
        except KeyError:
            return "El número introducido no es hexadecimal."
    return num_bin

def conversion_bin_dec(num_bin):
    num_bin = list(num_bin) 
    num_bin.reverse()
    num_dec = 0 
    for i in range(len(num_bin)): 
        num_dec += int(num_bin[i]) * 2 ** i 
    return num_dec

def maximo_hex(lista_hex):
    lista_dec = []
    for i in lista_hex:
        lista_dec.append(conversion_bin_dec(conversion_hex_bin(i)))
    max_dec = max(lista_dec)
    max_hex = lista_hex[lista_dec.index(max_dec)]
    return (max_hex, max_dec)

print("El número hexadecimal AA55 es", conversion_bin_dec(conversion_hex_bin("AA55")), "en binario.")

hex = ["AA55", "1010", "BEBE", "0101", "0FEA"] 
print(maximo_hex(hex))