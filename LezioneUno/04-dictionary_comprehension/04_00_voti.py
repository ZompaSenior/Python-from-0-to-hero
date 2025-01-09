voti = {'Luca': 7, 'Andrea': 8, 'Silvia': 9, 'Luigi': 5}

promossi = {}

for chiave, valore in voti.items():
    if(valore >= 6):
        promossi[chiave] = valore

for chiave in voti.keys():
    print(chiave)
    
print(promossi)
