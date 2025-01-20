"""Lettura di un file riga per riga!
   Scopriamo cosa c'è scritto in 'file.txt'!"""

# Apriamo il file in modalità lettura
file_testo = open("file.txt")

# Iniziamo a leggere il file riga per riga
print("📖 Inizio della lettura del file...")

while True:
    riga = file_testo.readline()  # Leggiamo una riga dal file

    if riga == '':  # Se non ci sono più righe, usciamo dal ciclo
        print("🔚 Fine della lettura del file!")
        break
    else:  # Se c'è una riga, stampiamola
        print(riga.strip())  # Usando strip() per rimuovere eventuali spazi bianchi

# Chiudiamo il file (è sempre una buona pratica!)
file_testo.close()

# Per le facciotte vai qui ...
# 😂 https://emojipedia.org/
