"""
In questo esempio, esploreremo come utilizzare l'ereditarietà
in Python per creare classi che gestiscono il colore e
l'alimentazione di un'auto. Creeremo una classe Auto che
eredita da Colore e Alimentazione.
"""

class Colore:
    """Classe base per gestire il colore: perché anche le auto vogliono essere alla moda."""

    def __init__(self, default):
        # Impostiamo il colore di default al momento della creazione.
        self.__colore = default

    @property
    def colore(self):
        """Ottieni il colore attuale."""
        return self.__colore

    @colore.setter
    def colore(self, colore):
        """Aggiorna il colore dell'auto."""
        self.__colore = colore


class Alimentazione:
    """Classe base per l'alimentazione: benzina, diesel, elettrica... o forse ad aria?"""

    def __init__(self, default):
        # Impostiamo l'alimentazione di default al momento della creazione.
        self.__alimentazione = default

    @property
    def alimentazione(self):
        """Ottieni il tipo di alimentazione attuale."""
        return self.__alimentazione

    @alimentazione.setter
    def alimentazione(self, alimentazione):
        """Aggiorna il tipo di alimentazione."""
        self.__alimentazione = alimentazione


class Auto(Colore, Alimentazione):
    """L'automobile secondo Python: personalizzabile, ma senza optional costosissimi!"""

    def __init__(self, colore, alimentazione):
        # Inizializziamo entrambe le classi genitore.
        Colore.__init__(self, colore)
        Alimentazione.__init__(self, alimentazione)


# Creiamo una nuova macchina con colore "Bianco" e alimentazione "Benzina".
macchina = Auto("Bianco", "Benzina")

# Stampiamo il colore iniziale.
print(f"Colore iniziale dell'auto: {macchina.colore}")

# Cambiamo il colore dell'auto in "Rosso" (un classico per le auto sportive).
macchina.colore = "Rosso"

# Stampiamo il nuovo colore dell'auto.
print(f"Colore aggiornato dell'auto: {macchina.colore}")

# E se vogliamo, possiamo aggiungere un esempio con alimentazione.
print(f"Tipo di alimentazione dell'auto: {macchina.alimentazione}")
