"""Come tutte le variabili, le funzioni possono essere passate come parametro
ad un'altra funzione."""

def chiamatore(a, b, operazione):
    return operazione(a, b)

def somma(a, b):
    return a + b

def moltiplicazione(a, b):
    return a * b


print(chiamatore(5, 7, somma))

print(chiamatore(5, 7, moltiplicazione))


