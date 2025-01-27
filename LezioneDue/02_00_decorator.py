"""
Questo esempio mostra come usare i decoratori per aggiungere comportamenti extra
alle funzioni: uno decoratore per stampare messaggi "Prima" e "Dopo", e un altro
per misurare il tempo di esecuzione di una funzione.
"""

import time

# Decoratore che aggiunge messaggi "Prima" e "Dopo" attorno alla funzione.
def scrittore(function):
    """
    Decoratore che stampa messaggi prima e dopo l'esecuzione della funzione.
    """
    def function_wrapper():
        print('Prima')  # Messaggio prima dell'esecuzione.
        function()  # Chiama la funzione originale.
        print('Dopo')  # Messaggio dopo l'esecuzione.
    return function_wrapper

# Applichiamo il decoratore `scrittore` alla funzione `chiamata`.
@scrittore
def chiamata():
    """Una semplice funzione che stampa un messaggio."""
    print('Durante')


# Decoratore che misura il tempo di esecuzione di una funzione.
def tempo(function):
    """
    Decoratore che misura il tempo di esecuzione di una funzione.
    """
    def function_wrapper():
        prima = time.time()  # Prendiamo il tempo iniziale.
        function()  # Eseguiamo la funzione originale.
        durata = time.time() - prima  # Calcoliamo il tempo trascorso.
        print(f"Tempo di esecuzione: {durata:.6f} secondi")  # Stampiamo il risultato.

    return function_wrapper

# Applichiamo il decoratore `tempo` alla funzione `chiamata2`.
@tempo
def chiamata2():
    """Una funzione che simula un carico di lavoro con un ciclo."""
    var = 0
    for i in range(1000):
        var += i


# Chiamiamo la funzione decorata con `scrittore`.
chiamata()

# Chiamiamo la funzione decorata con `tempo`.
chiamata2()



