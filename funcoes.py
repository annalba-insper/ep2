import random

def rolar_dados(numero_dados):
    lista = []
    i = 0
    while i < numero_dados:
        resultado = random.randint(1, 6)
        lista.append(resultado)
        i += 1
    return lista