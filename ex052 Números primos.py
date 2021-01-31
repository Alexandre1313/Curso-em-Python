numer = int(input('Digite um número:  '))
contador = 0
for x in range(1, numer + 1):
    if numer % x == 0:
        contador = contador + 1
        print(f'\033[32m{x}\033[m', end=' ')
    else:
        print(f'\033[35m{x}\033[m', end=' ')
print()
if contador == 2:
    print(f'O número \033[31m{numer}\033[m é um número primo')
    print(f'Pois foi divisível \033[32m{contador}\033[m vezes no intervalo entre 1 e ele mesmo')
else:
    print(f'O número \033[31m{numer}\033[m não é um número primo')
    print(f'Pois foi divisível \033[32m{contador}\033[m vezes no intervalo entre 1 e ele mesmo')
