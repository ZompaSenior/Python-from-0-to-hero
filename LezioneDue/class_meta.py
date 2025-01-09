# -*- coding: cp1252 -*-

import enum
import abc

class Veicolo(abc.ABC):
    """Il veicolo secono Python."""
    @property
    @abc.abstractmethod
    def colore(self):
        print("Abstract method.")

    @colore.setter
    @abc.abstractmethod
    def colore(self, colore):
        pass

    def pippo(self):
        print("Pippo")
    

class Auto(Veicolo):
    """L'automobile secono Python."""

    def __init__(self):
        self.__colore = "Bianco"

    @property
    def colore(self):
        super().colore
        return self.__colore

    @colore.setter
    def colore(self, colore):
        self.__colore = colore


macchina = Auto()

print(macchina.colore)

macchina.colore = "Rosso"

print(macchina.colore)

print(macchina.pippo())
