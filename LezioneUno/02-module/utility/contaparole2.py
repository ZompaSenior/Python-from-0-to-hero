def Conta():
    frase = input('Inserire una frase: ')

    parole = frase.split()

    conteggio = len(parole)

    print('Nella frase "%s" si sono %d parole.' % (frase, conteggio) )

    for numero, parola in enumerate(parole):
        print( '%d. %s' % (numero, parola) )

if __name__ == '__main__':
    Conta()
    
else:
    print("Nome modulo: %s" % (__name__, ))

