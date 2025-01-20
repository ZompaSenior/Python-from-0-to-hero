"""Import di sottomoduli: è comodo, ma occhio a non esagerare!"""

# Qui stiamo importando direttamente 'path' dal modulo 'sys'.
# Comodo? Certo! Ma rende meno chiaro da dove arriva 'path'.
from sys import path

# Stampiamo il contenuto di 'path'. Ricorda, è la lista dei percorsi
# dove Python va a cercare i moduli. È come il GPS di Python!
print("Ecco i percorsi di ricerca dei moduli (via 'from sys import path'):")
for p in path:
    print(f" - {p}")

# Nota di stile:
# Importare singole parti di un modulo va bene se sai cosa stai facendo
# (o se hai fretta). Però, se esageri, il codice diventa meno leggibile:
# chi legge potrebbe chiedersi "Da dove arriva 'path'?".

