"""List Comprehension: 
   Il modo super elegante e veloce per filtrare i numeri! 
   Dì addio ai metodi noiosi e abbraccia la bellezza del Python!"""

# Lista di numeri da cui estrarre i pari
numeri = [1, 2, 3, 4, 56, 77, 89, 21]

# Utilizziamo la list comprehension per ottenere i numeri pari
pari_pythonico = [numero for numero in numeri if numero % 2 == 0]

# Stampiamo i numeri pari trovati!
print(pari_pythonico)  # Risultato: [2, 4, 56]

