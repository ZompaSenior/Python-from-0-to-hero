"""Le funzioni possono essere usate come decoratori."""

def prefisso(function):
    print('Prima. ', end = '')

    return function

@prefisso
def chiamata():
    print('Output')


chiamata()


