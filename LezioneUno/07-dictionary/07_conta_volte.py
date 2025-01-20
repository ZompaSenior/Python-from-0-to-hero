"""Conta l'occorrenza di una parola in un file di testo."""

# Creiamo un dizionario per tenere traccia dei conteggi delle parole
conteggi = dict()

# Apriamo il file in modalità lettura usando 'with'
with open("file.txt") as file_testo:
    print("📖 Inizio del conteggio delle parole nel file...")
    
    # Leggiamo il file riga per riga
    for riga in file_testo:
        # Splittiamo la riga in parole e aggiorniamo i conteggi
        for parola in riga.strip().split():
            conteggi[parola] = conteggi.get(parola, 0) + 1  # Incrementiamo il conteggio della parola

# Stampiamo i risultati
print("\n📊 Conteggio delle parole:")
for parola, conteggio in conteggi.items():
    print(f"{parola}: {conteggio}")  # Mostriamo la parola e il suo conteggio

print("🔚 Conteggio completato!")  # Messaggio di fine conteggio

