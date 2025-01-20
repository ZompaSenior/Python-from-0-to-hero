"""List Comprehension: 
   Come NON fare le cose! 
   Ecco un modo lungo e noioso per ottenere i numeri pari!"""

# Lista di numeri da cui estrarre i pari
numeri = [1, 2, 3, 4, 56, 77, 89, 21]

# Iniziamo con una lista vuota per i numeri pari
pari = []

# Cicliamo attraverso i numeri, come se fossimo in un labirinto!
for numero in numeri:
    if numero % 2 == 0:
        pari.append(numero)  # Aggiungiamo i numeri pari, ma che fatica!

# Stampiamo i numeri pari trovati!
print(pari)  # Risultato: [2, 4, 56]

