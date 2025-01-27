"""
In questo esempio, esploreremo come definire una classe in Python
e utilizzare le enumerazioni (Enum) per rappresentare i colori
disponibili per un'auto. Creeremo una classe Auto con un colore
predefinito e la possibilità di cambiarlo.
"""

import enum

class Auto:
    """L'automobile secondo Python: più stilosa di quelle vere!"""

    # Una classe Enum per definire i colori disponibili.
    # Usiamo @enum.unique per assicurarci che i valori dei colori siano unici.
    @enum.unique
    class Colore(enum.Enum):
        BIANCO = 1
        NERO = 2
        ROSSO = 3
        VERDE = 4

    # Colore predefinito dell'auto (un po' come la personalità di default).
    __colore_preferito = Colore.BIANCO

    def __init__(self):
        # Ogni nuova auto inizia con il colore preferito (BIANCO).
        self.__colore = Auto.__colore_preferito

    @property
    def colore(self):
        """Il colore attuale dell'auto."""
        return self.__colore

    @colore.setter
    def colore(self, colore):
        """Permette di cambiare il colore dell'auto."""
        self.__colore = colore

    @classmethod
    def colore_preferito(cls):
        """Restituisce il colore preferito di tutte le auto."""
        return cls.__colore_preferito


# Creiamo una nuova macchina (BIANCA, perché è il colore preferito).
macchina = Auto()

# Stampiamo il colore iniziale dell'auto.
print(f"Colore iniziale dell'auto: {macchina.colore}")

# Cambiamo il colore dell'auto in ROSSO. (Un po' più grintoso!)
macchina.colore = Auto.Colore.ROSSO

# Stampiamo il nuovo colore dell'auto.
print(f"Colore aggiornato dell'auto: {macchina.colore}")

# Controlliamo il colore preferito delle auto (BIANCO).
print(f"Colore preferito delle auto: {Auto.colore_preferito()}")
