"""
In questo esempio, esploreremo come gestire le eccezioni in Python
utilizzando i blocchi try-except. Vedremo anche l'uso di assert.
"""

lista = [1, 2, 3]

# Proviamo a stampare un elemento fuori dai limiti della lista
try:
    print(lista[4])  # Questo solleverà un'eccezione IndexError
except IndexError as err:
    print(err)  # Stampa l'errore: list index out of range

# Proviamo a stampare una variabile non definita
# variabile = 3  # Questa riga è commentata per evitare un errore

try:
    print(variabile)  # Questo solleverà un'eccezione NameError
except IndexError as err:
    print(err)  # Non verrà mai eseguito
except Exception as e:  # Catturiamo qualsiasi altra eccezione
    print("Bho")  # Stampa "Bho" se si verifica un'eccezione
else:
    print("Tutto be.")  # Questo verrà eseguito solo se non ci sono eccezioni

# assert(3 > 4)  # Questa riga è commentata per evitare un'eccezione AssertionError
