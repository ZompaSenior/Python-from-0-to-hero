# Calcolatrice

def Calcola():
    # Chiedo il primo numero
    primo = int(input('Immetti un numero: '))

    # Chiedo il secodo numero
    secondo = int(input('Immetti un altro numero: '))

    operazione = 0
    
    # Continuo a chiedere l'operazione finche non ne viene indicata una valida
    while(operazione == 0 ):
        operazione =input('Che operazione desideri eseguire?\n(1. Somma\n2. Sottrazione\n3. Moltiplicazione\n4. Divisione)\n')
        operazione = int(operazione)    
        if(operazione == 1):
            risultato = primo + secondo
        elif(operazione == 2):
            risultato = primo - secondo
        elif(operazione == 3):
            risultato = primo * secondo
        elif(operazione == 4):
            risultato = primo / secondo
        else:
            operazione = 0
            # Messaggio d'errore
            print('\nSelezionare un operazione valida!\n')

    # Scrivo il risultato
    print("Il risultato e': %d" % ( risultato ) )

if __name__ == '__main__':
    Calcola()

else:
    print(f"{__name__} è stato importato.")
