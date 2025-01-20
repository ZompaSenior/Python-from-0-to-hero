"""Come tutte le variabili, le funzioni possono essere passate come parametro
ad un'altra funzione."""

def chiamatore(a, b, operazione):
    """Esegue l'operazione fornita su a e b."""
    return operazione(a, b)

def somma(a, b):
    """Restituisce la somma di a e b."""
    return a + b

def moltiplicazione(a, b):
    """Restituisce il prodotto di a e b."""
    return a * b

# Utilizziamo la funzione chiamatore con somma e moltiplicazione
print("Risultato della somma:", chiamatore(5, 7, somma))  # Dovrebbe stampare 12
print("Risultato della moltiplicazione:", chiamatore(5, 7, moltiplicazione))  # Dovrebbe stampare 35

