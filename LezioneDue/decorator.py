# -*- coding: cp1252 -*-
import time

def scrittore(function):
    def function_wrapper():
        print('Prima')
        function()
        print('Dopo')
    return function_wrapper

@scrittore
def chiamata():
    print('Durante')

def tempo(function):
    def function_wrapper():
        prima = time.time()
        function()
        print(f"tempo di esecuzione {time.time() - prima}")
    return function_wrapper

@tempo
def chiamata2():
    var = 0
    for i in range(1000):
        var += i

chiamata()
chiamata2()



