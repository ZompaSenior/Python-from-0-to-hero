# -*- coding: cp1252 -*-

import enum 

class Auto():
    """L'automobile secono Python."""

    @enum.unique
    class Colore(enum.Enum):
        BIANCO = 1
        NERO = 2
        ROSSO = 3
        VERDE = 4

    __colore_preferito = Colore.BIANCO
    
    def __init__(self):
        self.__colore = Auto.__colore_preferito

    @property
    def colore(self):
        return self.__colore

    @colore.setter
    def colore(self, colore):
        self.__colore = colore

    @classmethod
    def colore_preferito(cls):
        print(cls.colore)
        return cls.__colore_preferito


macchina = Auto()

print(macchina.colore)

macchina.colore = Auto.Colore.ROSSO

print(macchina.colore)

print(Auto.colore_preferito())

print(Auto.colore)
