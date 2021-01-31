lista = list()
for c in range(0, 7):
    numer = int(input(f'Digite o \033[36m{c + 1}º\033[m valor:  '))
    if c == 0 or numer > lista[-1] and numer not in lista:
        lista.append(numer)
        print('\033[31mADICIONADO NO FINAL DA LISTA\033[m...')
    else:
        pos = 0
        while pos < len(lista):
            if numer <= lista[pos] and numer not in lista:
                lista.insert(pos, numer)
                print(f'\033[31mADICIONADO NA POSIÇÃO {pos} DA LISTA\033[m...')
                break
            pos = pos + 1
print('=-'*20)
print('Sua lista em ordem crescente ficou assim: ', end='')
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        print(f'\033[32m{lista[c]}\033[m ', end='')
    else:
        print(f'\033[33m{lista[c]}\033[m ', end='')
print()
print('=-'*20)
