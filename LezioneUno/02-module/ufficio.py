"""Utility da ufficio"""

import utility.calcolatrice as calcola
import utility.contaparole as conta

def main():
    continua = True

    while(continua):
        selezione = int(input("""
    Che strumento vuoi usare?
        1. Contaparole
        2. Calcolatrice
        3. Uscire
        >"""))

        if(selezione == 1):
            conta.Conta()
            
        elif(selezione == 2):
            calcola.Calcola()
            
        elif(selezione == 3):
            continua = False
            
        else:
            print('\nSelezione non valida riprova.\n')
        
if(__name__ == "__main__"):
    main()
