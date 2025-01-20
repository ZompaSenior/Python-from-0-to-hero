"""List Comprehension Annidata: 
   Quando le liste si uniscono per creare una matrice! 
   E poi le appiattiamo come se fossero pancake!"""

import random

# Creiamo una matrice 3x3 con numeri casuali
matrice = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

# Stampiamo la matrice originale
print("Matrice originale:")
for riga in matrice:
    print(riga)

# Utilizziamo la list comprehension annidata per appiattire la matrice
lista_appiattita = [numero for riga in matrice for numero in riga]

# Stampiamo la lista appiattita
print("\nLista appiattita:")
print(lista_appiattita)

