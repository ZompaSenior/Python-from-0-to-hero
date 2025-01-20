"""Numero di parametri indefinito, ma con il nome! 
   Qui impariamo a usare i parametri con chiavi."""

def nome_funzione6(**chiavi):
    # Scorriamo le chiavi e i valori come se fossimo in un mercatino!
    for key, value in chiavi.items():
        # Stampiamo ogni chiave e il suo valore, come un cartellino del prezzo!
        print(key, '=', value)

# Chiamata alla funzione con parametri nominati
nome_funzione6(primo=1, secondo=2)  
# Output: primo = 1
#         secondo = 2

# Questa chiamata darà errore perché non possiamo mescolare posizionali e nominati
# nome_funzione6(3, primo=1, secondo=2)  # Commentato per evitare errori

