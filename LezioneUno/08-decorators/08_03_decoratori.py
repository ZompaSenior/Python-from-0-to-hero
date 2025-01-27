class Pippo():
    """Classe con delle proprietà"""

    def __init__(self):
        self.__valore = 3

    @property
    def valore(self):
        return self.__valore

    @valore.setter
    def valore(self, value):
        self.__valore = value

p = Pippo()

print(p.valore)
p.valore = 5

print(p.valore)
