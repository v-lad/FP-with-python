from inspect import signature, getfullargspec, getargspec
from partial import nonkw_partial

def sum4(a, b, c, d):
    return a + b + c + d

def curry(fn):
    l = len(signature(fn).parameters)
    copy_l = l
    
    def curried(fn):        

        def currying(*args):
            nonlocal l

            if l > len(args):
                f = nonkw_partial(fn, *args)
                l -= len(args)
                return curried(f)
            else:
                l = copy_l
                return fn(*args)

        return currying

    return curried(fn)

f = curry(sum4)
print(f(1, 2, 3, 4))
print(f(1)(2, 3, 4))
print(f(1, 2)(3, 4))
print(f(1, 2, 3)(4))
print(f(1)(2)(3, 4))
print(f(1)(2)(3)(4))
print(f(1)(2, 3)(4))
print(f(1, 2)(3)(4))