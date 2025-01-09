# -*- coding: cp1252 -*-

lista = [1, 2, 3]

try:
    print(lista[4])
except IndexError as err:
    print(err)

# variabile = 3

try:
    print(variabile)
except IndexError as err:
    print(err)
except:
    print("Bho")
else:
    print("Tutto be.")

# assert(3 > 4)
