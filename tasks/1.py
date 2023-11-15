from typing import Callable, TypeVar


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


T = TypeVar('T')


def task1(fun: Callable[[...], T], *args, **kwargs) -> T:
    print(f'Функция {fun.__name__} начала выполнение')
    r = fun(*args, **kwargs)
    if r is not None:
        print(f'Результат: {r}')
    print(f'Функция {fun.__name__} завершила выполнение')
    return r


task1(factorial, 5)