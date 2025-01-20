"""Dizionari: 
   Come NON fare le cose! 
   Ecco un modo lungo e noioso per calcolare i promossi!"""

# Dizionario dei voti degli studenti
voti = {'Luca': 7, 'Andrea': 8, 'Silvia': 9, 'Luigi': 5}

# Metodo tradizionale per calcolare i promossi
promossi = {}

# Eleneco studenti
print("Elenchiamo gli studenti:")
for chiave in voti.keys():
    print(chiave)

# Calcolo i promossi, come se fosse una maratona!
print("\nCalcoliamo i promossi:")
for chiave, valore in voti.items():
    if valore >= 6:
        promossi[chiave] = valore  # Aggiungiamo i promossi al dizionario

# e li stampo
print("\nPromossi (metodo tradizionale):")
print(promossi)

