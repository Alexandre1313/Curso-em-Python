numer = int(input('Digite um número para ver seu fatorial:  '))
cont = numer
fact = 1
print(f'\033[31mCalculando {numer}! fatorial:\033[m')
while cont > 0:
    print(f'\033[32m{cont}\033[m ', end='')
    print('\033[33mx\033[m 'if cont > 1 else '= ', end='')
    fact = fact * cont
    cont = cont - 1
print(f'\033[33m{fact}\033[m')

# exemplo utilizando o for

numer = int(input('Digite um número para ver seu fatorial:  '))
fact = 1
print(f'\033[31mCalculando {numer}! fatorial:\033[m')
for c in range(numer, 0, -1):
    print(f'\033[32m{c}\033[m ', end='')
    print('\033[33mx\033[m ' if c > 1 else '= ', end='')
    fact = fact * c
print(f'\033[33m{fact}\033[m')
