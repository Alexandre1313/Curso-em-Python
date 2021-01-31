lista = [[], []]
for c in range(1, 8):
    numer = int(input(f'Informe o \033[31m{c}º\033[m valor:  '))
    if numer % 2 == 0:
        lista[0].append(numer)
    else:
        lista[1].append(numer)
lista[0].sort()
lista[1].sort()
print('Sua lista de números  pares se compõe  como segue:  ', end='')
for lis in lista[0]:
    print(f'\033[32m{lis}\033[m  ', end='')
print()
print('Sua lista de números ímpares se compõe como segue:  ', end='')
for lis in lista[1]:
    print(f'\033[31m{lis}\033[m  ', end='')
print()
