"""
In questo esempio, esploreremo la tecnica di unpacking degli argomenti
nelle funzioni. Utilizzeremo sia le liste che i dizionari per passare
gli argomenti alla funzione.
"""

def funzione(primo, secondo, terzo):
    # Questa funzione restituisce il risultato di primo + secondo * terzo
    return primo + secondo * terzo

# Liste di argomenti
lista = [1, 2, 3]
lista2 = [7, 5, 8]

# Utilizziamo l'unpacking per passare gli argomenti dalla lista
print(funzione(*lista))   # Output: 7
print(funzione(*lista2))  # Output: 51

# Dizionari di argomenti
dizionario = {'secondo': 4, 'primo': 3, 'terzo': 5}
print(funzione(**dizionario))  # Output: 23

dizionario2 = {'primo': 3, 'secondo': 4}
# Qui mancano gli argomenti, quindi si otterrà un errore
# print(funzione(**dizionario2))  # Uncomment per vedere l'errore
