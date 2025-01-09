# -*- coding: cp1252 -*-

def primo(val):
    return val[0]

coppie = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
coppie.sort(key=lambda paia: paia[1])
print(coppie)

coppie = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
coppie.sort(key=primo)
print(coppie)
