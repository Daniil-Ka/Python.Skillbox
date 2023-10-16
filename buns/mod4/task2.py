def power(a: float, n: int) -> float:
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(a, -n)
    elif n % 2 == 0:
        return power(a * a, n // 2)
    return a * power(a, n - 1)


a, n = input('Введите a и n: ').split()
a = float(a)
n = int(n)
print(power(a, n))
