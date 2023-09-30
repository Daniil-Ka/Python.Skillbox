a = input()
print('no' if ((sum(map(int, a[::2])) + sum(map(int, a[1::2])) * 3) % 10) else 'yes')
