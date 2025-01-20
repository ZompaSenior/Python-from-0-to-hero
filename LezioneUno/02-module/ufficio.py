"""Utility da ufficio: 
   Un programma che ti offre strumenti per contare parole e fare calcoli! 
   Perfetto per chi ama tenere tutto sotto controllo!"""

import utility.calcolatrice as calcola
import utility.contaparole as conta

def main():
    """Funzione principale: il cuore pulsante del nostro ufficio virtuale!"""
    continua = True

    while continua:
        selezione = int(input("""\
Che strumento vuoi usare? 
    1. Contaparole (per chi ama le parole!)
    2. Calcolatrice (per i matematici in erba!)
    3. Uscire (ma perché? Non vuoi divertirti?)
> """))

        if selezione == 1:
            # Chiamiamo il contaparole, pronto a contare come un campione!
            conta.Conta()
        
        elif selezione == 2:
            # Chiamiamo la calcolatrice, per fare un po' di magia matematica!
            calcola.Calcola()
        
        elif selezione == 3:
            # Uscita dal programma, ma ci mancherai!
            continua = False
        
        else:
            # Selezione non valida, facciamo sapere all'utente che ha sbagliato!
            print('\nSelezione non valida, riprova! Dai, non è così difficile!\n')

if __name__ == "__main__":
    main()

