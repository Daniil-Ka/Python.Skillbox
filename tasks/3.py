from typing import Callable, TypeVar
import math

T = TypeVar('T')
def task3(func):
    def wrapper(*args, **kwargs):
        print(f"Начало выполнения функции {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Завершение выполнения функции {func.__name__}")
        return result
    return wrapper

@task3
def factorial(n):
    return math.factorial(n)


print(factorial(5))
