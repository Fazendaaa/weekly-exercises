import sys
from typing import Any, Callable

sys.setrecursionlimit(1_500_000)


def memoize(func) -> Callable[..., Any]:
    cache = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    wrapper.clear_cache = lambda: cache.clear()

    return wrapper


@memoize
def fibonacci(n: int) -> int | Any:
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(1_000))
# print(sum(i for i in range(1, 100_000) if fib(i) % 2 == 0))
