"""Le funzioni sono Oggetti e possono essere usate come variabili"""

def funzione(a, b):
    return a * b

pippo = funzione
pluto = funzione

print(pippo(2, 3))
print(pluto(4, 6))
print(funzione(7, 2))

print(funzione)

print(pippo.__name__)
