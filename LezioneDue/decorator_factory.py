# -*- coding: cp1252 -*-

def before_run(logging=True):
    def decorator(func):
        print("hello from before run")
        def handle_arg(a,b):
            if(a>0):
                if logging:
                    print "Altering argument a to 100"
                a = 100
            return func(a,b)

        return handle_arg

    return decorator
