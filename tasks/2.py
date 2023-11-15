from typing import Callable, TypeVar
import time

def task1(fun: Callable[[...], T], *args, **kwargs) -> T:
    start = time.time()
    r = fun(*args, **kwargs)
    end = time.time()
    print(end - start)
    return r

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


T = TypeVar('T')





task1(factorial, 100)