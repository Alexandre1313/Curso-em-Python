from random import randint
from time import sleep
from operator import itemgetter
dado = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6),
        'Jogador5': randint(1, 6),
        'Jogador6': randint(1, 6),
        'Jogador7': randint(1, 6)}
ranking = list()
efeito0 = 'JOGO DE DADO'
print('\033[31m*\033[m' * 40)
for c in efeito0:
    print(f'\033[33;1m{f"{c}":^1}\033[m', end=''), sleep(0.3)
print()
print('\033[31m*\033[m' * 40)
print('\033[31m-\033[m' * 40)
for k, v in dado.items():
    print(f'\033[32m{k}\033[m \033[31mtirou\033[m \033[32m{v}\033[m \033[31mno dado\033[m')
    print('\033[31m-\033[m' * 40)
    sleep(1)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
cont = 1
efeito = 'RESULTADO'
print('\033[31m*\033[m' * 40)
for c in efeito:
    print(f'\033[33;1m{f"{c}":^1}\033[m', end=''), sleep(0.3)
print()
print('\033[31m*\033[m' * 40)
print('\033[31m-\033[m' * 40)
for i, v in ranking:
    print(f'\033[31mEm\033[m \033[32m{cont}º\033[m \033[31mlugar\033[m \033[32m{i}\033[m \033[31mque ', end='')
    print(f'tirou\033[m \033[32m{v}\033[m \033[31mno dado\033[m')
    cont = cont + 1
    print('\033[31m-\033[m' * 40)
    sleep(1)
efeito1 = 'PROGRAMA FINALIZADO'
print('\033[31m*\033[m' * 40)
for c in efeito1:
    print(f'\033[33;1m{f"{c}":^1}\033[m', end=''), sleep(0.3)
print()
print('\033[31m*\033[m' * 40)
