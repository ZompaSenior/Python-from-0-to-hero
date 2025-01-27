"""Esempio di decoratore che lavora sui parametri di una funzione."""

def manipola_parametri(funzione):
    """Un decoratore che modifica i parametri e il risultato della funzione."""
    def wrapper(*args, **kwargs):
        # Stampiamo i parametri originali
        print(f"Parametri originali: args={args}, kwargs={kwargs}")
        
        # Modifichiamo i parametri (ad esempio raddoppiamo i numeri interi)
        nuovi_args = tuple(arg * 2 if isinstance(arg, int) else arg for arg in args)
        nuovi_kwargs = {k: v * 2 if isinstance(v, int) else v for k, v in kwargs.items()}
        print(f"Parametri modificati: args={nuovi_args}, kwargs={nuovi_kwargs}")
        
        # Chiamiamo la funzione originale con i nuovi parametri
        risultato = funzione(*nuovi_args, **nuovi_kwargs)
        
        # Modifichiamo il risultato (ad esempio, moltiplichiamo per 10)
        print(f"Risultato originale: {risultato}")
        risultato_modificato = risultato * 10 if isinstance(risultato, int) else risultato
        print(f"Risultato modificato: {risultato_modificato}")
        
        return risultato_modificato
    return wrapper

@manipola_parametri
def somma(a, b=0):
    """Somma due numeri."""
    return a + b

# Chiamiamo la funzione decorata
print(somma(3, b=7))  # Esempio con argomenti posizionali e keyword
