
class fp:
    pass

fp.fmap_none = lambda fn, x: (fn(x) if x else None)


def maybe(x):
    def fmap(fn):
        return fp.maybe(fp.fmap_none(fn, x))

    def apply(functor):
        return functor(lambda fn: fp.fmap_none(fn, x))
    fmap.apply = apply

    def chain(fnM):
        return fnM(x)
    fmap.chain = chain

    return fmap

fp.maybe = maybe

# fp.maybe(5)(lambda x: x**2)(lambda x: x+2)(print)
# fp.maybe(5)(lambda x: x**2).apply(fp.maybe(lambda x: x*2))(print)
# fp.maybe(5)(lambda x: x**2).chain(lambda x: fp.maybe(x+10))(print)

def half(x):
    res = x / 2 
    return fp.maybe(int(res)) if x % 2 == 0 else fp.maybe(None)


fp.maybe(40).chain(half).chain(half).chain(half)(print)

