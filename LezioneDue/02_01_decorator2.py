"""
In questo esempio, esploreremo come utilizzare i decoratori per
modificare il comportamento delle funzioni. Abbiamo due decoratori:
uno per "escapare" le parentesi graffe nelle stringhe e l'altro
per stampare il risultato della funzione.
"""

def escape_args(original_function):
    # Questo decoratore si occupa di "escapare" le parentesi graffe
    # nelle stringhe
    def new_function(*args, **kwargs):
        # Modifichiamo gli argomenti: se è una stringa, sostituiamo
        # '{' con '{{' e '}' con '}}'
        args = [
            arg.replace('{', '{{').replace('}', '}}') 
            if isinstance(arg, str) else arg 
            for arg in args
        ]
        # Chiamiamo la funzione originale con gli argomenti modificati
        return original_function(*args, **kwargs)

    return new_function

def print_result(original_function):
    # Questo decoratore stampa il risultato della funzione originale
    def new_function(*args, **kwargs):
        # Chiamiamo la funzione originale e salviamo il valore restituito
        returned_value = original_function(*args, **kwargs)
        # Stampiamo il valore restituito con un messaggio
        print(returned_value, "--secondo")
        return returned_value

    return new_function

@escape_args
@print_result
def pippo(a, b, c):
    # Questa è la funzione principale che stampa i suoi argomenti
    print(a, b, c, "--primo")
    return (a, b, c)

# Eseguiamo la funzione pippo con alcuni argomenti
pippo("Ciao", 3, "kajsnxkjan{kkn}")
