"""
In questo esempio, esploreremo come utilizzare le funzioni
per creare funzioni lambda che possono essere utilizzate
per incrementare un valore.
"""

def incrementatore(n):
    # Questa funzione restituisce una funzione lambda che
    # incrementa un valore x di n
    return lambda x: x + n

# Creiamo due funzioni incrementatrici
test = incrementatore(5)   # Incrementa di 5
test2 = incrementatore(10)  # Incrementa di 10

# Testiamo le funzioni incrementatrici
print(test(3))   # Output: 8 (3 + 5)
print(test2(3))  # Output: 13 (3 + 10)
