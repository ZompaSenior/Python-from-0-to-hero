"""
In questo esempio, esploreremo come definire una classe in Python
e utilizzare i getter e setter per gestire gli attributi privati.
Creeremo una classe Auto con un colore predefinito e la possibilità
di cambiarlo, dimostrando anche l'accesso diretto agli attributi privati.
"""

class Auto:
    """L'automobile secondo Python: sempre elegante (e bianca di default)."""

    def __init__(self):
        # Il colore dell'auto è privato (con il doppio underscore) e parte da "Bianco".
        self.__colore = "Bianco"

    @property
    def colore(self):
        """Getter per il colore dell'auto."""
        return self.__colore

    @colore.setter
    def colore(self, colore):
        """Setter per il colore dell'auto."""
        self.__colore = colore


# Creiamo una macchina, di default è "Bianca".
macchina = Auto()

# Stampiamo il colore iniziale.
print(f"Colore iniziale dell'auto: {macchina.colore}")

# Cambiamo il colore della macchina in "Rosso".
macchina.colore = "Rosso"

# Stampiamo il nuovo colore.
print(f"Colore aggiornato dell'auto: {macchina.colore}")

# Accesso al colore direttamente (e un po' illegalmente) usando il nome "mangling".
# Questo non è raccomandato, ma dimostra che il doppio underscore non è
# un muro invalicabile, ma più un "cartello di avviso".
print(f"Accesso diretto al colore privato: {macchina._Auto__colore}")
