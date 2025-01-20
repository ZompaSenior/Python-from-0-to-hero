import pprint

"""Dizionari Annidati: 
   I voti degli studenti in diverse materie! 
   Scopriamo chi è il campione delle materie!"""

# Dizionario annidato con i voti degli studenti
voti = {
    'Luca': {'Matematica': 8, 'Italiano': 7, 'Storia': 9},
    'Andrea': {'Matematica': 6, 'Italiano': 8, 'Storia': 7},
    'Silvia': {'Matematica': 9, 'Italiano': 9, 'Storia': 10},
    'Luigi': {'Matematica': 5, 'Italiano': 6, 'Storia': 5}
}

# Stampiamo i voti in modo carino
print("Voti degli studenti:")
pprint.pprint(voti)

# Calcoliamo la media dei voti per ogni studente usando la dict comprehension
medie = {studente: sum(materie.values()) / len(materie) for studente, materie in voti.items()}

# Stampiamo le medie in modo ordinato
print("\nMedie dei voti:")
for studente, media in medie.items():
    print(f"{studente}: {media:.2f}")  # Formattiamo la media a due decimali

# Troviamo il miglior studente
miglior_studente = max(medie, key=medie.get)
print(f"\nIl miglior studente è {miglior_studente} con una media di {medie[miglior_studente]:.2f}!")

