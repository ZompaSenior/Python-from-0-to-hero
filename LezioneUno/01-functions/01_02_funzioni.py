"""Numero di parametri indefinito! 
   Qui impariamo a gestire un numero variabile di argomenti."""

def nome_funzione3(*values):
    # Iniziamo la nostra somma a zero, come un contabile in ferie!
    somma = 0
    for n in values:
        # Aggiungiamo ogni numero alla somma, come se non ci fosse un domani!
        somma += n
    return somma

# Chiamata alla funzione con un sacco di numeri
print(nome_funzione3(1, 2, 3, 55, 99))  # Risultato: 160

def nome_funzione4(*values):
    # Usando la funzione built-in sum per fare il lavoro sporco!
    return sum(values)

# Chiamata alla funzione con altri numeri
print(nome_funzione4(3, 44, 55, 66))  # Risultato: 168

def nome_funzione5(primo, secondo, *altri):
    # Sommiamo i primi due e poi il resto della festa!
    return primo + secondo + sum(altri)

# Chiamata alla funzione con un mix di numeri
print(nome_funzione5(11, 22, 67, 55, 66))  # Risultato: 221

