for n in range(2, 11):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'igual', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'é um número primo.')
for c in reversed(range(1,10)):
    print(c)
print(bin(1259))
