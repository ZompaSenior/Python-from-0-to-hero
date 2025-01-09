# -*- coding: cp1252 -*-

class auto():
    """L'automobile secono Python."""

    def __init__(self):
        self.__colore = "Bianco"

    @property
    def colore(self):
        return self.__colore

    @colore.setter
    def colore(self, colore):
        self.__colore = colore

macchina = auto()

print(macchina.colore)

macchina.colore = "Rosso"

print(macchina.colore)

print(macchina._auto__colore)
