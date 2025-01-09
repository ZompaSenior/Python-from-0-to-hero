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

    class Alimentazione(enum.Enum):
        BENZINA = enum.auto()
        GASOLIO = enum.auto()
        GPL = enum.auto()
        METANO = enum.auto()
        
    def __init__(self):
        self.__colore = Auto.Colore.BIANCO
        self.__alimentazione = Auto.Alimentazione.BENZINA

    @property
    def colore(self):
        return self.__colore

    @colore.setter
    def colore(self, colore):
        if(isinstance(colore, Auto.Colore)):
            self.__colore = colore
        else:
            print(colore, " non è un parametro valido.")

    @property
    def alimentazione(self):
        return self.__alimentazione

    @alimentazione.setter
    def alimentazione(self, alimentazione):
        self.__alimentazione = alimentazione

    @staticmethod
    def print_colori():
        for colore in Auto.Colore.__members__.keys():
            print(colore)


macchina = Auto()

print(macchina.colore)

macchina.colore = "Rosso"

print(macchina.colore)

Auto.print_colori()

