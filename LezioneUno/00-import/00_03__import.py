"""Import 'all': il metodo pigro che ti farà pentire delle tue scelte!"""

# Con 'from sys import *' importiamo tutto dal modulo 'sys'.
# Sembra comodo? Non proprio. Importare tutto:
# - Usa più memoria (carichi roba che non ti serve).
# - Rende il codice meno chiaro (non sai cosa viene importato).
# Quindi... evitiamolo quando possibile!
from sys import *

# Stampiamo 'path' come esempio. Ma attenzione, questo stile di importazione
# rende il codice poco leggibile e rischia di causare conflitti di nomi.
print("Percorsi di ricerca dei moduli (import 'all'):")
for p in path:
    print(f" - {p}")

# Nota importante:
# Non usare 'from module import *' a meno che tu non abbia una buona ragione,
# tipo: "Voglio far soffrire chi leggerà il mio codice!" 😉

