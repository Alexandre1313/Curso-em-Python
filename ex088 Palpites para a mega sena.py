from random import randint
from time import sleep

print('\033[31m=\033[m' * 42)
print(f'\033[33m{"JOGOS PARA MEGA SENA":^42}\033[m')
print('\033[31m=\033[m' * 42)
quant = int(input('\033[32mQuantos jogos deseja sortear?:\033[m        '))
print('\033[31m=\033[m' * 42)
jogos = []
jogo = []
cont = 1
c = 0
while cont <= quant:
    while len(jogo) < 6:
        for c in range(0, 1):
            numer = randint(1, 60)
            if numer not in jogo:
                jogo.append(numer)
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    cont = cont + 1
print('\033[33mSegue abaixo lista dos jogos solicitados:\033[m')
print('\033[31m=\033[m' * 42)
for l in jogos:
    if c < 9:
        print(f'\n\033[32m0{c + 1}º\033[m \033[31mjogo:\033[m ', end=''), sleep(0.5)
    else:
        print(f'\n\033[32m{c + 1}º\033[m \033[31mjogo:\033[m ', end=''), sleep(0.5)
    c = c + 1
    for el in l:
        if el < 10:
            print(f'\033[36m0{el}\033[m    ', end=''), sleep(0.5)
        else:
            print(f'\033[36m{el}\033[m    ', end=''), sleep(0.5)
print('\n')
print('\033[31m=\033[m' * 42)
print(f'\033[33m{f"Foram sorteados ao todo {len(jogos)} jogos":^42}\033[m')
print('\033[31m=\033[m' * 42)
print(f'\033[33m{"BOA SORTE!!!":^42}\033[m')
print('\033[31m=\033[m' * 42)
