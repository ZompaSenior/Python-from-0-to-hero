"""Calcolatrice: il tuo assistente personale per i numeri!"""

def Calcola():
    """Funzione che esegue operazioni matematiche di base. Preparati a fare i conti!"""
    
    # Chiedo il primo numero, non essere timido!
    primo = int(input('Immetti un numero: '))
    
    # Chiedo il secondo numero, perché uno non basta mai!
    secondo = int(input('Immetti un altro numero: '))
    
    operazione = 0
    
    # Continuo a chiedere l'operazione finché non ne viene indicata una valida
    while operazione == 0:
        operazione = input('Che operazione desideri eseguire?\n(1. Somma\n2. Sottrazione\n3. Moltiplicazione\n4. Divisione)\n')
        
        # Proviamo a convertire l'input in un intero
        try:
            operazione = int(operazione)
        except ValueError:
            print("Ops! Devi inserire un numero, non una lettera!")
            continue
        
        # Eseguiamo l'operazione scelta
        if operazione == 1:
            risultato = primo + secondo
            print(f"Il risultato della somma è: {risultato}")
        elif operazione == 2:
            risultato = primo - secondo
            print(f"Il risultato della sottrazione è: {risultato}")
        elif operazione == 3:
            risultato = primo * secondo
            print(f"Il risultato della moltiplicazione è: {risultato}")
        elif operazione == 4:
            if secondo != 0:
                risultato = primo / secondo
                print(f"Il risultato della divisione è: {risultato}")
            else:
                print("Non puoi dividere per zero! Riprova.")
                operazione = 0  # Reset operazione per richiedere di nuovo
        else:
            operazione = 0
            # Messaggio d'errore
            print('\nSeleziona un\'operazione valida, dai!\n')

if __name__ == '__main__':
    Calcola()
else:
    print(f"{__name__} è stato importato.")

