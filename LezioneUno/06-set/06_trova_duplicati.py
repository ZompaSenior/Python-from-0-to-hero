# -*- coding: cp1252 -*-

univoci = set()

with open("file.txt") as file_testo:
    for numero_riga, riga in enumerate(file_testo, 1):
        if (riga in univoci):
            print("Trovato duplicato alla riga", numero_riga)
        else:
            univoci.add(riga)

