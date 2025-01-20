"""Le funzioni possono essere usate come decoratori."""

def prefisso(function):
    """Un decoratore che aggiunge un prefisso all'output della funzione."""
    def wrapper():
        print('Prima. ', end='')  # Stampa il prefisso
        function()  # Chiama la funzione originale
    return wrapper  # Restituisce la funzione decorata

@prefisso  # Applica il decoratore alla funzione chiamata
def chiamata():
    """Funzione che stampa un messaggio."""
    print('Output')

# Chiamiamo la funzione decorata
chiamata()  # Dovrebbe stampare "Prima. Output"

