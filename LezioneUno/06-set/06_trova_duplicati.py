"""Controllo dei duplicati in un file!
   Scopriamo se ci sono righe duplicate in 'file.txt'!"""

# Creiamo un set per tenere traccia delle righe uniche
univoci = set()

# Apriamo il file in modalità lettura usando 'with'
with open("file.txt") as file_testo:
    print("📖 Inizio della scansione del file per duplicati...")
    
    # Leggiamo il file riga per riga, tenendo traccia del numero di riga
    for numero_riga, riga in enumerate(file_testo, 1):
        if riga.strip() in univoci:  # Controlliamo se la riga è già stata vista
            print("Trovato duplicato alla riga", numero_riga)
        else:  # Se la riga è unica, la aggiungiamo al set
            univoci.add(riga.strip())  # Aggiungiamo la riga senza spazi bianchi

print("🔚 Scansione completata!")  # Messaggio di fine scansione

