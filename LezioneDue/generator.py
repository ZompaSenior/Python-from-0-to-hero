# -*- coding: cp1252 -*-

def mesi_generator():
    yield("Gennaio")
    yield("Febbraio")
    yield("Marzo")
    yield("Aprile")
    yield("Maggio")
    yield("Giugno")
    yield("Luglio")
    yield("Agosto")
    yield("Settembre")
    yield("Ottobre")
    yield("Novembre")
    yield("Dicembre")

def numeri_generator():
    for i in range(10):
        yield(i)

mesi = mesi_generator()

try:
    print(next(mesi))
    print(next(mesi))
    print(next(mesi))
    print(next(mesi))
    print(next(mesi))
    print(next(mesi))
    print(next(mesi))
    print(next(mesi))
    print(next(mesi))
    print(next(mesi))
    print(next(mesi))
    print(next(mesi))
    print(next(mesi))
except StopIteration:
    print("Mesi finiti")


for numero in numeri_generator():
    print(numero)

