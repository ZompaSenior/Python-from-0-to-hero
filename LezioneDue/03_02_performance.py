"""
Ehi, amico! Oggi esploriamo tre modi diversi per calcolare i quadrati dei numeri da 0 a 9999.
Useremo un ciclo for, una list comprehension e un generatore con yield.
Alla fine, vedremo anche quale metodo è più veloce. Pronto? Iniziamo!
"""

import timeit

# Funzione per il ciclo for
def ciclo_for():
    quadrati = []
    for i in range(10000):
        quadrati.append(i ** 2)
    return quadrati

# Funzione per la list comprehension
def list_comprehension():
    quadrati = [i ** 2 for i in range(10000)]
    return quadrati

# Funzione per il generatore con yield
def generatore():
    for i in range(10000):
        yield i ** 2

# Misuriamo le prestazioni
if __name__ == "__main__":
    # Tempo per il ciclo for
    tempo_for = timeit.timeit(ciclo_for, number=1000)
    print(f"Tempo ciclo for: {tempo_for:.5f} secondi")

    # Tempo per la list comprehension
    tempo_list_comp = timeit.timeit(list_comprehension, number=1000)
    print(f"Tempo list comprehension: {tempo_list_comp:.5f} secondi")

    # Tempo per il generatore
    tempo_generatore = timeit.timeit(lambda: list(generatore()), number=1000)
    print(f"Tempo generatore: {tempo_generatore:.5f} secondi")
