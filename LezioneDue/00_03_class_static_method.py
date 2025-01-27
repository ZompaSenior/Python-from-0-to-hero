"""
Questo esempio illustra come utilizzare gli Enum in Python per rappresentare
colori e tipi di alimentazione di un'automobile. Dimostra anche come usare
getter e setter con controlli di validità per garantire l'integrità dei dati.
"""

import enum

class Auto:
    """L'automobile secondo Python: personalizzabile con colori e alimentazioni!"""

    # Enum per i colori disponibili.
    @enum.unique
    class Colore(enum.Enum):
        BIANCO = 1
        NERO = 2
        ROSSO = 3
        VERDE = 4

    # Enum per i tipi di alimentazione.
    class Alimentazione(enum.Enum):
        BENZINA = enum.auto()
        GASOLIO = enum.auto()
        GPL = enum.auto()
        METANO = enum.auto()

    def __init__(self):
        # Impostiamo il colore e l'alimentazione di default.
        self.__colore = Auto.Colore.BIANCO
        self.__alimentazione = Auto.Alimentazione.BENZINA

    @property
    def colore(self):
        """Ottieni il colore attuale dell'auto."""
        return self.__colore

    @colore.setter
    def colore(self, colore):
        """Imposta il colore dell'auto, ma solo se è un valore valido dell'Enum."""
        if isinstance(colore, Auto.Colore):
            self.__colore = colore
        else:
            print(f"{colore} non è un colore valido! Usa Auto.Colore.")

    @property
    def alimentazione(self):
        """Ottieni il tipo di alimentazione dell'auto."""
        return self.__alimentazione

    @alimentazione.setter
    def alimentazione(self, alimentazione):
        """Imposta l'alimentazione dell'auto."""
        if isinstance(alimentazione, Auto.Alimentazione):
            self.__alimentazione = alimentazione
        else:
            print(f"{alimentazione} non è un'alimentazione valida!")

    @staticmethod
    def print_colori():
        """Stampa tutti i colori disponibili."""
        print("Colori disponibili per l'auto:")
        for colore in Auto.Colore.__members__.keys():
            print(f" - {colore}")


# Creiamo una macchina con i valori di default (colore BIANCO, alimentazione BENZINA).
macchina = Auto()

# Stampiamo il colore iniziale dell'auto.
print(f"Colore iniziale dell'auto: {macchina.colore}")

# Proviamo a impostare un colore non valido.
macchina.colore = "Rosso"  # Questo darà un errore perché non è un valore Enum.

# Stampiamo il colore attuale (dovrebbe essere ancora BIANCO).
print(f"Colore attuale dell'auto: {macchina.colore}")

# Stampiamo tutti i colori disponibili.
Auto.print_colori()
