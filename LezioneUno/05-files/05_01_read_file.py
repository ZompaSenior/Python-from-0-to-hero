"""Lettura di un file riga per riga!
   Scopriamo cosa c'è scritto in 'file.txt'!"""

# Apriamo il file in modalità lettura usando 'with'
with open("file.txt") as file_testo:
    print("📖 Inizio della lettura del file...")
    
    # Leggiamo il file riga per riga
    for riga in file_testo:
        print(riga.strip())  # Usando strip() per rimuovere eventuali spazi bianchi

print("🔚 Fine della lettura del file!")  # Messaggio di fine lettura

