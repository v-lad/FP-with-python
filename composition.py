from functools import reduce


def compose2(f1, f2):
    return lambda x: f2(f1(x))


def compose(*funcs):
    return reduce(lambda a, b: compose2(a, b), funcs)


def inc(a):
    return a+1


double_inc = compose2(inc, inc)
print(double_inc(10))

triple_inc = compose(inc, inc, inc)
print(triple_inc(1))
