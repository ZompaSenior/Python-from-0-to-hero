"""
Definizione dell'eccezione personalizzata
"""

class ValoreNegativoErrore(Exception):
    """Eccezione sollevata quando si tenta di impostare un valore negativo."""
    pass

class Contatore:
    def __init__(self):
        self.valore = 0

    @property
    def valore(self):
        return self.valore

    @valore.setter
    def valore(self, nuovo_valore):
        if nuovo_valore < 0:
            raise ValoreNegativoErrore("Il valore non può essere negativo!")
        self.valore = nuovo_valore

# Esempio di utilizzo
if __name__ == "__main__":
    contatore = Contatore()

    try:
        contatore.imposta_valore(10)
        print(f"Valore impostato: {contatore.ottieni_valore()}")

        # Tentativo di impostare un valore negativo
        contatore.imposta_valore(-5)
    except ValoreNegativoErrore as e:
        print(f"Errore: {e}")
