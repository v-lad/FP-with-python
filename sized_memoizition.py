from time import monotonic_ns
from collections import OrderedDict


def generate_key(args):
    return hash(args)


def memoize(*, size=float('inf')):
    def memoize_decorator(f):
        cache = OrderedDict()
        
        def wrapper(*args, **kwargs):
            nonlocal cache
            key = generate_key((*args, *kwargs.items()))
            val = cache.get(key)

            if val:
                return val                     

            res = f(*args, **kwargs)

            if len(cache) >= size:
                cache.popitem()

            cache[key] = res
            return res

        return wrapper
    return memoize_decorator


@memoize(size=1000)
def fibonacci(n):
    return 1 if n <= 2 else fibonacci(n-1)+fibonacci(n-2)


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10000)

    t1 = monotonic_ns()
    (lambda n: 1 if n <= 2 else fibonacci(n-1)+fibonacci(n-2))(500)
    print(f't1 = {round(monotonic_ns() - t1, 5)}')

    t2 = monotonic_ns()
    fibonacci(500)
    print(f't2 = {round(monotonic_ns() - t2, 5)}')

    # print(len(fibonacci.__closure__[0].cell_contents))
