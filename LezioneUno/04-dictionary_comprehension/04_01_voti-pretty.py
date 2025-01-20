"""Dizionari: 
   Il modo elegante e veloce per calcolare i promossi! 
   Dì addio ai metodi noiosi e abbraccia la bellezza della dictionary comprehension!"""

# Dizionario dei voti degli studenti
voti = {'Luca': 7, 'Andrea': 8, 'Silvia': 9, 'Luigi': 5}

# Calcolo i promossi con la dictionary comprehension
promossi = {chiave: valore for chiave, valore in voti.items() if valore >= 6}

# Stampiamo i promossi, come se avessimo appena vinto alla lotteria!
print("Promossi (con dictionary comprehension):")
print(promossi)

