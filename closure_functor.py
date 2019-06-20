

def functor(x=None):
    return lambda fmap: functor(fmap(x)) if x and fmap else functor(x)


functor(2)(lambda x: x**2)(lambda x: x+2)(None)(lambda x: x+1)(print)
functor(None)(print)

def apply_functor(x=None):
    
    def fmap(fn):
        return apply_functor(fn(x) if x else None)

    def apply(fnA):
        return fnA(lambda fn: fn(x) if fn else x)

    fmap.apply = apply

    return fmap

a = apply_functor(2)  # x = 2; return fmap
f1 = apply_functor(lambda x: x*4)  # x = fn; return fmap---

a.apply(f1)(print)

# print(f1.__closure__[0].cell_contents)
# print(a.__closure__[0].cell_contents)


