def Conta():
    frase = input('Inserire una frase: ')

    parole = frase.split(' ')

    conteggio = len(parole)

    print('Nella frase "%s" si sono %d parole.' % (frase, conteggio) )

    numero = 1

    for parola in parole:
        print( '%d. %s' % (numero, parola) )
        numero += 1

if __name__ == '__main__':
    Conta()

else:
    print(f"{__name__} è stato importato.")
