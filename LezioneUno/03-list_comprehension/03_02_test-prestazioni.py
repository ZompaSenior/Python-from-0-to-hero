import random
import timeit

"""List Comprehension vs. Metodo Tradizionale: 
   Chi vincerà nella corsa per ottenere i numeri pari? 
   Scopriamolo con un po' di numeri casuali!"""

# Generiamo una lista di 1.000.000 di numeri casuali tra 1 e 100
numeri = [random.randint(1, 100) for _ in range(1_000_000)]

# Funzione per il metodo tradizionale
def metodo_tradizionale():
    pari = []
    for numero in numeri:
        if numero % 2 == 0:
            pari.append(numero)
    return pari

# Funzione per il metodo con list comprehension
def metodo_pythonico():
    return [numero for numero in numeri if numero % 2 == 0]

# Misuriamo il tempo impiegato dal metodo tradizionale
tempo_tradizionale = timeit.timeit(metodo_tradizionale, number=10)
print(f"Tempo con metodo tradizionale: {tempo_tradizionale:.4f} secondi")

# Misuriamo il tempo impiegato dal metodo con list comprehension
tempo_pythonico = timeit.timeit(metodo_pythonico, number=10)
print(f"Tempo con list comprehension: {tempo_pythonico:.4f} secondi")

# Confrontiamo i risultati
if tempo_tradizionale < tempo_pythonico:
    print("Il metodo tradizionale ha vinto! Ma non è un vero campione...")
else:
    print("La list comprehension ha vinto! Elegante e veloce!")

