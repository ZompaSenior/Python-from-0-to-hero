"""
In questo esempio, esploreremo i generatori in Python. I generatori
sono una forma di iteratore che permette di generare valori su richiesta
utilizzando la parola chiave 'yield'.
"""

def mesi_generator():
    # Generatore che restituisce i nomi dei mesi
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
    # Generatore che restituisce i numeri da 0 a 9
    for i in range(10):
        yield(i)

# Creiamo un'istanza del generatore dei mesi
mesi = mesi_generator()

# Proviamo a stampare i mesi uno alla volta
try:
    print(next(mesi))  # Gennaio
    print(next(mesi))  # Febbraio
    print(next(mesi))  # Marzo
    print(next(mesi))  # Aprile
    print(next(mesi))  # Maggio
    print(next(mesi))  # Giugno
    print(next(mesi))  # Luglio
    print(next(mesi))  # Agosto
    print(next(mesi))  # Settembre
    print(next(mesi))  # Ottobre
    print(next(mesi))  # Novembre
    print(next(mesi))  # Dicembre
    print(next(mesi))  # Genera un'eccezione StopIteration
    
except StopIteration:
    print("Mesi finiti")  # Messaggio quando non ci sono più mesi

# Stampiamo i numeri generati
for numero in numeri_generator():
    print(numero)  # Stampa i numeri da 0 a 9
