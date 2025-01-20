"""Ehi, guarda come funziona l'import in Python!"""

# Importiamo il modulo 'sys'. Perché? Beh, perché è figo 
# e ci dice un sacco di cose sull'ambiente Python.
import sys

# Ok, ora stampiamo 'sys.path'. Cos'è 'sys.path'?
# In pratica è la lista dei posti dove Python va a cercare i moduli
# quando diciamo "import".
print("Ecco dove Python va a curiosare per cercare i moduli (sys.path):")
for path in sys.path:
    print(f" - {path}")

# Prova tu!
# Se lanci questo script, vedrai che il primo percorso nella lista è
# proprio la directory corrente. È come dire: "Prima controllo in casa mia,
# poi vedo nel resto del mondo!"
# E ora sai perché Python riesce a trovare i tuoi file .py nella stessa
# cartella. Magia? No, solo sys.path. 😎

