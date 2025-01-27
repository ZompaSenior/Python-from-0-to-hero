"""
In questo esempio, esploreremo come generare coppie di numeri
utilizzando la funzione zip e una funzione interna per creare
una lista di base.
"""

def coppie_doppie(numero_coppie):
    # Funzione interna che crea una lista di base
    def crea_lista_base(dimensione):
        return range(dimensione)

    # Restituiamo le coppie di numeri utilizzando zip
    return zip(crea_lista_base(numero_coppie),
               crea_lista_base(numero_coppie * 2),
               crea_lista_base(numero_coppie * 3))

# Stampiamo le coppie generate per 5 coppie
for coppia in coppie_doppie(5):
    print(coppia)  # Output: (0, 0, 0), (1, 2, 3), (2, 4, 6), (3, 6, 9), (4, 8, 12)

# Stampiamo le coppie generate per 3 coppie
for a, b, c in coppie_doppie(3):
    print(a, b, c)  # Output: 0 0 0, 1 2 3, 2 4 6
