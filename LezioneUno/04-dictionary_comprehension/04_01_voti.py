voti = {'Luca': 7, 'Andrea': 8, 'Silvia': 9, 'Luigi': 5}

promossi = {chiave: valore for chiave, valore in voti.items() if valore >= 6}

print(promossi)
