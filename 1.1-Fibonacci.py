# fib4 - caches decorated functions output for set of inputs
from functools import lru_cache
from typing import Generator  # fib 6

# fib3 - caches function input/output using a dictionary object
from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}


def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)


def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)


def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]


@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 2) + fib4(n - 1)


def fib5(n: int) -> int:
    if n == 0:
        return n  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next


def fib6(n: int) -> Generator[int, None, None]:
    yield 0  # special case
    if n > 0:
        yield 1  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next


if __name__ == "__main__":
    print('Optimized Fibonacci Sequence')
    print(fib5(5))
    print(fib5(10))
    print(fib5(50))

    print('Printing Each step of fib(50)')
    for i in fib6(50):
        print(i)
