lis = []
c = 1
for c in range(1, 5):
    nu1 = float(input(f'Digite o {c}º valor:  '))
    lis.append(nu1)

print(f'{sorted(lis)}')
for v in lis:
    print(f'\033[33m{v}\033[m')
