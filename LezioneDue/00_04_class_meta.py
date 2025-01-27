"""
In questo esempio, esploreremo come utilizzare le classi astratte
in Python per definire un'interfaccia per i veicoli. Creeremo
una classe base astratta 'Veicolo' e una classe concreta 'Auto'
che implementa i metodi astratti.
"""

import enum
import abc

class Veicolo(abc.ABC):
    """Il veicolo secondo Python: un'idea astratta di mezzo di trasporto."""

    # Un metodo astratto per il colore. Deve essere implementato dalle sottoclassi!
    @property
    @abc.abstractmethod
    def colore(self):
        print("Questo metodo è astratto e deve essere implementato!")
        pass

    # Anche il setter per 'colore' è astratto. Le sottoclassi devono implementarlo.
    @colore.setter
    @abc.abstractmethod
    def colore(self, colore):
        pass

    # Metodo concreto: tutte le sottoclassi lo ereditano così com'è.
    def pippo(self):
        print("Sono Pippo, un metodo concreto definito nella classe base!")


class Auto(Veicolo):
    """L'automobile secondo Python: concreta e pronta a girare!"""

    def __init__(self):
        # Impostiamo un colore di default: Bianco (che eleganza!)
        self.__colore = "Bianco"

    @property
    def colore(self):
        # Superiamo la classe base, ma il suo metodo astratto non fa nulla.
        super().colore
        return self.__colore

    @colore.setter
    def colore(self, colore):
        # Cambiamo il colore della macchina.
        self.__colore = colore


# Creiamo una macchina (finalmente concreta, non astratta!).
macchina = Auto()

# Stampiamo il colore iniziale della macchina.
print(f"Colore iniziale dell'auto: {macchina.colore}")

# Cambiamo il colore della macchina in "Rosso" (non si può sbagliare con il rosso).
macchina.colore = "Rosso"

# Stampiamo il nuovo colore della macchina.
print(f"Colore aggiornato dell'auto: {macchina.colore}")

# Ecco 'Pippo', il metodo ereditato dalla classe astratta.
macchina.pippo()
