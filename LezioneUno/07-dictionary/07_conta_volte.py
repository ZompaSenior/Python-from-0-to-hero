"""Conta l'occorrenza di una parola in un file di testo."""

conteggi = dict()

with open("file.txt") as file_testo:
    for riga in file_testo:
        conteggi[riga.strip()] = conteggi.get(riga.strip(), 0) + 1

for parola, conteggio in conteggi.items():
    print(parola, conteggio)
