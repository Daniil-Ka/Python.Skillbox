def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = map(int, input('Введите a и b: ').split())
print(gcd(a, b))
