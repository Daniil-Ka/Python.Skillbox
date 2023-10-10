first_line = list(input().strip())
a = [first_line] + [list(input().strip()) for _ in range(len(first_line) - 1)]
lines = a + list(zip(*a)) + [[a[i][i] for i in range(len(a))]] + [[a[i][len(a) - i - 1] for i in range(len(a))]]
r = sum([[symbol for symbol in "XO" if line.count(symbol) >= len(a)] for line in lines], [])
print(r[0] if r else 'Ничья')
