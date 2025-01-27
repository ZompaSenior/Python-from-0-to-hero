"""
Esempio di decorator factory: un decoratore che può essere configurato 
tramite parametri. Questo permette di creare decoratori flessibili e riutilizzabili.
"""

def before_run(logging=True):
    """
    Decorator factory: restituisce un decoratore personalizzato in base al parametro
    `logging`. Permette di modificare il comportamento della funzione decorata.

    Args:
        logging (bool): Se True, abilita il logging delle modifiche sui parametri.

    Returns:
        function: Un decoratore che altera il comportamento della funzione decorata.
    """
    def decorator(func):
        print("Creazione del decoratore tramite la factory `before_run`.")

        def handle_arg(a, b):
            """
            Modifica il primo argomento (se maggiore di 0) e chiama la funzione decorata.

            Args:
                a: Il primo argomento della funzione decorata.
                b: Il secondo argomento della funzione decorata.

            Returns:
                Il risultato della funzione decorata.
            """
            if a > 0:
                if logging:  # Se il logging è abilitato, stampa un messaggio.
                    print("Modifico l'argomento 'a' a 100.")
                a = 100  # Alteriamo il valore di 'a'.
            return func(a, b)  # Chiamiamo la funzione decorata con gli argomenti aggiornati.

        return handle_arg

    return decorator

# Esempio di utilizzo della decorator factory:
@before_run(logging=True)  # Qui configuriamo il decoratore abilitando il logging.
def somma(a, b):
    """Esempio di funzione decorata che somma due numeri."""
    return a + b

# Test della funzione decorata:
print("Risultato della funzione somma(5, 10):", somma(5, 10))  # Cambia 'a' a 100.
print("Risultato della funzione somma(-5, 10):", somma(-5, 10))  # 'a' resta invariato.
