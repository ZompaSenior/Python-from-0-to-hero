# -*- coding: cp1252 -*-

def funzione(primo, secondo, terzo):
    return primo + secondo * terzo

lista = [1, 2, 3]

lista2 = [7, 5, 8]

print(funzione(*lista))

print(funzione(*lista2))

dizionario = {'secondo': 4, 'primo': 3, 'terzo': 5}
print(funzione(**dizionario))

dizionario2 = {'primo': 3, 'secondo': 4}
print(funzione(**dizionario2))
