"""
Oggi vediamo come funziona il ciclo for con range.
Preparati a contare da 0 a 4 in modo semplice e divertente!
"""

# Creiamo un oggetto range
r = range(5)  # Questo genera i numeri da 0 a 4

# Utilizziamo il ciclo for
print("Utilizzando il ciclo for con range:")
for numero in r:
    print(numero)

# Creiamo di nuovo l'oggetto range
r = range(5)

# Utilizziamo next() manualmente
print("\nUtilizzando next() con range:")
iteratore = iter(r)
while True:
    try:
        numero = next(iteratore)
        print(numero)
    except StopIteration:
        break
