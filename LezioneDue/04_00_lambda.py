"""
In questo esempio, esploreremo come ordinare una lista di tuple
utilizzando funzioni chiave. Utilizzeremo sia una funzione lambda
che una funzione definita dall'utente per determinare l'ordine.
"""

def primo(val):
    # Questa funzione restituisce il primo elemento della tupla
    return val[0]

# Lista di coppie (tupla)
coppie = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

# Ordinamento delle coppie in base al secondo elemento della tupla
coppie.sort(key=lambda paia: paia[1])
print(coppie)  # Output: [(1, 'one'), (4, 'four'), (3, 'three'), (2, 'two')]

# Ripristiniamo la lista originale
coppie = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

# Ordinamento delle coppie in base al primo elemento della tupla
coppie.sort(key=primo)
print(coppie)  # Output: [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
