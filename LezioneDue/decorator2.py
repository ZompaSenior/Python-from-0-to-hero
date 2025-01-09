# -*- coding: cp1252 -*-

def escape_args(original_function):
    def new_function(*args, **kwargs):
        args = [arg.replace('{', '{{').replace('}', '}}') if isinstance(arg, str) else arg for arg in args]
        return original_function(*args, **kwargs)

    return new_function

def print_result(original_function):
    def new_function(*args, **kwargs):
        returned_value = original_function(*args, **kwargs)
        print(returned_value, "--secondo")
        return returned_value

    return new_function

@escape_args
@print_result
def pippo(a, b, c):
    print(a, b, c, "--primo")
    return(a, b, c)

pippo("Ciao", 3, "kajsnxkjan{kkn}")
