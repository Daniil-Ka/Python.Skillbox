a, b = input().split(',')
print(len(a.split(b)[0]) + 1 if len(a) and a[0] == b else 0)
