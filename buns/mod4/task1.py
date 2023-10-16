ALL_EQUAL = 'Все числа равны'
ALL_DIFFERENT = 'Все числа разные'
EQUAL_AND_DIFFERENT = 'Есть равные и неравные числа'


def f(sp: list) -> str:
    unique_count = len(set(sp))
    if unique_count == 1:
        return ALL_EQUAL
    if len(sp) == unique_count:
        return ALL_DIFFERENT
    return EQUAL_AND_DIFFERENT


print(f([1, 1, 2]))
sp = list(map(int, input().split()))
print(f(sp))
