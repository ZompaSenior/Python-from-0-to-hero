"""Parametri opzionali. 
   Qui impariamo a impostare valori di default. 
   Ricorda: devono sempre essere gli ultimi!"""

def nome_funzione(primo_par, secondo_par, terzo_par=0):
    # Sommiamo i tre parametri, ma il terzo è opzionale!
    return primo_par + secondo_par + terzo_par

# Chiamata alla funzione con solo i primi due parametri
print(nome_funzione(3, 6))  # Risultato: 9 (3 + 6 + 0)

def nome_funzione2(primo_par=0, secondo_par=1, terzo_par=0):
    # Moltiplichiamo il primo per il secondo e aggiungiamo il terzo
    return primo_par * secondo_par + terzo_par

# Chiamata alla funzione con tutti i parametri di default
print(nome_funzione2(3, 6), end='\n\n\n')  # Risultato: 18 (3 * 6 + 0)

# Chiamata alla funzione con il terzo parametro specificato
print(nome_funzione2(3, terzo_par=6))  # Risultato: 9 (3 * 1 + 6)

