from time import monotonic_ns


def generate_key(args):
    return hash(args)


def memoize(f):
    cache = {}
    
    def wrapper(*args):
        nonlocal cache
        key = generate_key(args)
        val = cache.get(key)

        if val:
            return val
        
        res = f(*args)
        cache[key] = res
        return res

    return wrapper

@memoize
def fibonacci(n):
    return 1 if n <= 2 else fibonacci(n-1)+fibonacci(n-2)


t1 = monotonic_ns()
(lambda n: 1 if n <= 2 else fibonacci(n-1)+fibonacci(n-2))(500)
print(f't1 = {round(monotonic_ns() - t1, 5)}')

t2 = monotonic_ns()
fibonacci(500)
print(f't2 = {round(monotonic_ns() - t2, 5)}')
# print(fibonacci.__closure__[0].cell_contents)
