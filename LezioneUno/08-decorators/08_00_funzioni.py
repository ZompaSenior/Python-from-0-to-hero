"""Le funzioni sono oggetti e possono essere usate come variabili!"""

def funzione(a, b):
    """Moltiplica due numeri e restituisce il risultato."""
    return a * b

# Assegniamo la funzione a due variabili
pippo = funzione
pluto = funzione

# Utilizziamo le variabili per chiamare la funzione
print("Risultato di pippo(2, 3):", pippo(2, 3))  # Dovrebbe stampare 6
print("Risultato di pluto(4, 6):", pluto(4, 6))  # Dovrebbe stampare 24
print("Risultato di funzione(7, 2):", funzione(7, 2))  # Dovrebbe stampare 14

# Stampiamo la funzione stessa
print("\nLa funzione:", funzione)

# Stampiamo il nome della funzione
print("Il nome della funzione pippo è:", pippo.__name__)  # Dovrebbe stampare 'funzione'

