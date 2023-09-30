a = input()
gl, gc = 'аеиоуёюя', 0

for i in gl:
    gc += a.count(i)

print(gc, len(a) - a.count(' ') - gc)