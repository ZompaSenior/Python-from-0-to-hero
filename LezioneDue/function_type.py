# -*- coding: cp1252 -*-

def funzione(parametro: str) -> str:
    return "Risultato"

def funzione2(parametro: str) -> str:
    return 1

def funzione3(parametro: int) -> int:
    return "Abc"

print(funzione('abc'))

print(funzione2('abc'))

print(funzione2(3))

print(funzione3(4))

print(funzione3('abc'))
