"""Import con alias: pratico, ma scegli l'alias con cura!"""

# Qui importiamo il modulo 'sys' e gli diamo un alias, 's'.
# È utile per abbreviare nomi lunghi o usati spesso.
import sys as s

# Stampiamo il contenuto di 's.path'. È sempre la lista dei percorsi
# dove Python cerca i moduli, ma stavolta accediamo tramite 's'.
print("Percorsi di ricerca dei moduli (alias 's'):")
for p in s.path:
    print(f" - {p}")

# Nota di stile:
# Gli alias sono utili, ma fai attenzione a sceglierli bene!
# Usare nomi corti è comodo ('np' per NumPy è un classico),
# ma evitare nomi ambigui o poco intuitivi ti salva da grattacapi futuri.

