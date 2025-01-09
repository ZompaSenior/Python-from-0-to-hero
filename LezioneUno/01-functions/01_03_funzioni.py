"""Numero parametri indefinito, ma con il nome"""

def nome_funzione6(**chiavi):
    for key, value in chiavi.items():
        print(key, '=', value)

nome_funzione6(primo = 1, secondo = 2)

nome_funzione6(3, primo = 1, secondo = 2)

