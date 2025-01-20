"""
Contaparole: 
Un semplice strumento per contare le parole in una frase e mostrarle una per 
una!"""

def Conta():
    """Funzione che conta le parole in una frase e le elenca. Pronto a contare?"""
    
    # Chiediamo all'utente di inserire una frase
    frase = input('Inserire una frase: ')
    
    # Dividiamo la frase in parole, come un puzzle!
    parole = frase.split(' ')
    
    # Contiamo quante parole ci sono
    conteggio = len(parole)
    
    # Stampiamo il risultato del conteggio
    print('Nella frase "%s" ci sono %d parole.' % (frase, conteggio))
    
    numero = 1
    
    # Elenchiamo ogni parola con il suo numero
    for parola in parole:
        print('%d. %s' % (numero, parola))
        numero += 1

if __name__ == '__main__':
    Conta()
else:
    print(f"{__name__} è stato importato.")

