"""
In questo esempio, esploreremo la tipizzazione dei parametri e dei
valori di ritorno delle funzioni. Vedremo anche come il tipo di
argomento passato influisce sul comportamento della funzione.
"""

def funzione(parametro: str) -> str:
    # Questa funzione accetta una stringa e restituisce un risultato
    return "Risultato"

def funzione2(parametro: str) -> str:
    # Questa funzione accetta una stringa e restituisce un intero
    return 1

def funzione3(parametro: int) -> int:
    # Questa funzione accetta un intero ma restituisce una stringa
    return "Abc"

# Eseguiamo le funzioni con vari argomenti
print(funzione('abc'))        # Output: Risultato

print(funzione2('abc'))       # Output: 1

print(funzione2(3))           # Output: 1 (ma il parametro non è del tipo atteso)

print(funzione3(4))           # Output: Abc (ma il parametro è del tipo atteso)

print(funzione3('abc'))       # Errore: il parametro non è del tipo atteso
