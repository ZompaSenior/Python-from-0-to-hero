"""Parametri opzionali.
Bata impostare un valore di fefault.
Devono essere gli ultimi."""

def nome_funzione(primo_par, secondo_par, terzo_par = 0):
    return primo_par + secondo_par + terzo_par

print(nome_funzione(3, 6))


def nome_funzione2(primo_par = 0, secondo_par = 1, terzo_par = 0):
    return primo_par * secondo_par + terzo_par

print(nome_funzione2(3, 6), end='\n\n\n')

print(nome_funzione2(3, terzo_par = 6))
