# -*- coding: cp1252 -*-

class Colore():
    """Classe base per il colore."""

    def __init__(self, default):
        self.__colore = default

    @property
    def colore(self):
        return self.__colore

    @colore.setter
    def colore(self, colore):
        self.__colore = colore

class Alimentazione():
    """Classe base per l'alimentazione."""

    def __init__(self, default):
        self.__alimentazione = default

    @property
    def alimentazione(self):
        return self.__alimentazione

    @alimentazione.setter
    def alimentazione(self, alimentazione):
        self.__alimentazione = alimentazione


class Auto(Colore, Alimentazione):
    """L'automobile secono Python."""

    def __init__(self, colore, alimentazione):
        Colore.__init__(self, colore)
        Alimentazione.__init__(self, alimentazione)

macchina = Auto("Bianco", "Benzina")

print(macchina.colore)

macchina.colore = "Rosso"

print(macchina.colore)
