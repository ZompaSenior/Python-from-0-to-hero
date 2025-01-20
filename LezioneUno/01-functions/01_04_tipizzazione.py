"""Tipizzazione delle Funzioni in Python: 
   Le annotazioni di tipo aiutano a rendere il codice più leggibile 
   e a fornire indicazioni sui tipi di dati attesi, ma non sono vincolanti!"""

def somma(a: int, b: int) -> int:
    """Somma due numeri interi e restituisce il risultato."""
    return a + b

# Chiamata alla funzione con parametri corretti
print(somma(3, 4))  # Risultato: 7

# Ora vediamo che la tipizzazione non è vincolante!
# Possiamo passare anche tipi diversi, e Python non si lamenta!
print(somma(3.5, 4.2))  # Risultato: 7.7 (somma di float)
print(somma("3", "4"))  # Risultato: 34 (concatenazione di stringhe)

# Anche se non è quello che ci aspettiamo, Python è flessibile!

