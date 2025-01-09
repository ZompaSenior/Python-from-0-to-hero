# -*- coding: cp1252 -*-

def coppie_doppie(numero_coppie):
    def crea_lista_base(dimensione):
        return range(dimensione)

    return zip(crea_lista_base(numero_coppie),
               crea_lista_base(numero_coppie*2),
               crea_lista_base(numero_coppie*3))

for coppia in coppie_doppie(5):
    print(coppia)

for a, b, c in coppie_doppie(3):
    print(a, b, c)
