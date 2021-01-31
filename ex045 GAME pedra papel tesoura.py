from random import randint
from time import sleep
while True:
    itens = ('PEDRA', 'PAPEL', 'TESOURA')
    comp = randint(0, 2)
    print('\033[33mVAMOS JOGAR ? ESCOLHA UMA DAS OPÇÕES:\033[m')
    print('=-'*19)
    print('''\033[36m[1] PEDRA
[2] PAPEL
[3] TESOURA\033[m''')
    print('=-'*19)
    jogador = int(input('\033[36mSua jogada:\033[m  '))
    jogador1 = jogador - 1
    print('=-'*19)
    print('\033[31mJO\033[m', end='')
    sleep(1)
    print(' \033[32mKEM\033[m', end='')
    sleep(1)
    print(' \033[33mPÔ\033[m')
    sleep(1)
    print('=-'*19)
    print(f'Computador escolheu \033[33m{itens[comp]}\033[m')
    print(f'Jogador escolheu    \033[35m{itens[jogador1]}\033[m')
    print('=-'*19)
    if comp == 0:
        if jogador1 == 0:
            print('HOUVE EMPATE')
        elif jogador1 == 1:
            print('JOGADOR VENCE')
        elif jogador1 == 2:
            print('COMPUTADOR VENCE')
    elif comp == 1:
        if jogador1 == 0:
            print('COMPUTADOR VENCE')
        elif jogador1 == 1:
            print('HOUVE EMPATE')
        elif jogador1 == 2:
            print('JOGADOR VENCE')
    elif comp == 2:
        if jogador1 == 0:
            print('JOGADOR VENCE')
        elif jogador1 == 1:
            print('COMPUTADOR VENCE')
        elif jogador1 == 2:
            print('HOUVE EMPATE')
    resp = str(input("Deseja continuar?[S/N]:  ")).strip().upper()
    while resp not in 'SN':
        resp = str(input("Deseja continuar?[S/N]:  ")).strip().upper()
    if resp == 'N':
        break
print('=-'*19)
print('Fim...')
print('=-'*19)
