"""Contaparole2: 
   Un altro strumento per contare le parole in una frase, ma con un tocco di stile!"""

def Conta():
    """Funzione che conta le parole in una frase e le elenca. Pronto a contare?"""
    
    # Chiediamo all'utente di inserire una frase
    frase = input('Inserire una frase: ')
    
    # Dividiamo la frase in parole, senza specificare il delimitatore!
    parole = frase.split()
    
    # Contiamo quante parole ci sono
    conteggio = len(parole)
    
    # Stampiamo il risultato del conteggio
    print('Nella frase "%s" ci sono %d parole.' % (frase, conteggio))
    
    # Elenchiamo ogni parola con il suo numero, come in un elenco telefonico!
    for numero, parola in enumerate(parole):
        print('%d. %s' % (numero + 1, parola))  # Aggiungiamo 1 per iniziare da 1

if __name__ == '__main__':
    Conta()
else:
    print("Nome modulo: %s" % (__name__,))

