
def partial_single(fn, x):
    return lambda *args: fn(x, *args)


def partial(fn, *args, **kwargs):
    return lambda *rest, **kwrest: fn(*(list(args) + list(rest)), **kwargs, **kwrest)

def nonkw_partial(fn, *args):
    return lambda *rest: fn(*(list(args) + list(rest)))

def sum4(a, b, c, d):
    return a + b + c + d


def main():
    f11 = partial_single(sum4, 1)
    f12 = partial_single(f11, 2)
    f13 = partial_single(f12, 3)
    y = f13(4)

    print()
    print(y)
    print()

    f21 = partial(sum4, 1, 2)
    f22 = partial(f21, 3)
    y2 = f22(4)

    print(y2)
    print()


    def testp(a, b, c, *, d=None):
        print(a, b, c, d)

    f1 = partial(testp, d=2)
    f1(1, 2, 3)

if __name__ == "__main__":
    main()