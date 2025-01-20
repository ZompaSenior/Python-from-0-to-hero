"""Restituzione multipla da funzioni: quando una cosa non basta!"""

# Ecco una funzione che restituisce due valori.
# Python ti permette di farlo in modo super comodo (senza dover usare un 
# dizionario o una lista).
def funzione_inutile():
    return 1, 2  # Restituiamo due valori come una tupla

# Qui "a" e "b" ricevono i valori dalla tupla restuita dalla funzione
# È come se 'funzione_inutile()' restituisse una scatola con due cose dentro,
# e noi le estraiamo con l'assegnazione.
a, b = funzione_inutile()

# Stampiamo i valori ottenuti
print(a, b)  # Ecco il risultato: 1 2

