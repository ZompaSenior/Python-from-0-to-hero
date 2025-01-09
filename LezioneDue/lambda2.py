# -*- coding: cp1252 -*-

def incrementatore(n):
    return lambda x: x + n

test = incrementatore(5)
test2 = incrementatore(10)
print(test(3))
print(test2(3))
