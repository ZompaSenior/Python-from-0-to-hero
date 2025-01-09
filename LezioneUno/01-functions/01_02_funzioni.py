"""Numero di parametri indefinito"""

def nome_funzione3(*values):
    somma = 0
    for n in values:
        somma += n

    return somma

print(nome_funzione3(1, 2, 3, 55, 99))


def nome_funzione4(*values):
    return sum(values)

print(nome_funzione4(3, 44, 55, 66))


def nome_funzione5(primo, secondo, *altri):
    return primo + secondo + sum(altri)

print(nome_funzione5(11, 22, 67, 55, 66))


