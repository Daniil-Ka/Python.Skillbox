def print_matrix(m):
    [print(*r, sep=', ') for r in m]
    print()


a = int(input())
m = [list(range(1, a + 1)) for _ in range(a)]
print_matrix(m)
t = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print_matrix(t)