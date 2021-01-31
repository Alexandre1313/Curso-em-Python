from time import sleep
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somaimpar = totp = toti = totm = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'\033[31mDigite um valor para\033[m [\033[31m{l}\033[m, \033[31m{c}\033[m]:  '))
        if matriz[l][c] % 2 == 0:
            totp = totp + 1
        else:
            toti = toti + 1
print('\033[31m=-\033[m'*14)
print(f'\033[33m{"MATRIZ PYTHON":^28}\033[m')
print('\033[31m=-\033[m'*14)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'\033[33m[\033[m\033[32m{matriz[l][c]:^7}\033[m\033[33m]\033[m', end='')
    print()
print('\033[31m=-\033[m'*14)
sleep(2)
print(f'\033[31mMatriz com\033[m \033[32m{totp}\033[m \033[31melementos  par, os  quais são:\033[m  ', end='')
for l in matriz:
    for c in l:
        if c % 2 == 0:
            print(f'\033[32m{c}\033[m  ', end='')
            somapar = somapar + c
print()
print(f'\033[31mA  soma  de todos os elementos par é:\033[m \033[32m{somapar}\033[m')
sleep(2)
print(f'\033[31mMatriz com\033[m \033[32m{toti}\033[m \033[31melementos ímpar, os quais são:\033[m  ', end='')
for l in matriz:
    for c in l:
        if c % 2 == 1:
            print(f'\033[32m{c}\033[m  ', end='')
            somaimpar = somaimpar + c
print()
print(f'\033[31mA soma de todos os elementos ímpar é:\033[m \033[32m{somaimpar}\033[m')
sleep(2)
somacol1 = matriz[0][0] + matriz[1][0] + matriz[2][0]
somacol2 = matriz[0][1] + matriz[1][1] + matriz[2][1]
somacol3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'\033[31mA soma de todos os elementos da coluna\033[m \033[32m1\033[m \033[31mé:\033[m \033[32m{somacol1}\033[m')
sleep(2)
print(f'\033[31mA soma de todos os elementos da coluna\033[m \033[33m2\033[m \033[31mé:\033[m \033[32m{somacol2}\033[m')
sleep(2)
print(f'\033[31mA soma de todos os elementos da coluna\033[m \033[36m3\033[m \033[31mé:\033[m \033[32m{somacol3}\033[m')
sleep(2)
somal1 = matriz[0][0] + matriz[0][1] + matriz[0][2]
somal2 = matriz[1][0] + matriz[1][1] + matriz[1][2]
somal3 = matriz[2][0] + matriz[2][1] + matriz[2][2]
print(f'\033[31mA soma  de todos os elementos da linha\033[m \033[32m1\033[m \033[31mé:\033[m \033[32m{somal1}\033[m')
sleep(2)
print(f'\033[31mA soma  de todos os elementos da linha\033[m \033[33m2\033[m \033[31mé:\033[m \033[32m{somal2}\033[m')
sleep(2)
print(f'\033[31mA soma  de todos os elementos da linha\033[m \033[36m3\033[m \033[31mé:\033[m \033[32m{somal3}\033[m')
sleep(2)
maicol1 = matriz[0][0], matriz[1][0], matriz[2][0]
maicol2 = matriz[0][1], matriz[1][1], matriz[2][1]
maicol3 = matriz[0][2], matriz[1][2], matriz[2][2]
print(f'\033[31mO maior valor da coluna\033[m \033[32m1\033[m \033[31mé:\033[m \033[32m{max(maicol1)}\033[m')
sleep(2)
print(f'\033[31mO maior valor da coluna\033[m \033[33m2\033[m \033[31mé:\033[m \033[32m{max(maicol2)}\033[m')
sleep(2)
print(f'\033[31mO maior valor da coluna\033[m \033[36m3\033[m \033[31mé:\033[m \033[32m{max(maicol3)}\033[m')
sleep(2)
mencol1 = matriz[0][0], matriz[1][0], matriz[2][0]
mencol2 = matriz[0][1], matriz[1][1], matriz[2][1]
mencol3 = matriz[0][2], matriz[1][2], matriz[2][2]
print(f'\033[31mO menor valor da coluna\033[m \033[32m1\033[m \033[31mé:\033[m \033[32m{min(mencol1)}\033[m')
sleep(2)
print(f'\033[31mO menor valor da coluna\033[m \033[33m2\033[m \033[31mé:\033[m \033[32m{min(mencol2)}\033[m')
sleep(2)
print(f'\033[31mO menor valor da coluna\033[m \033[36m3\033[m \033[31mé:\033[m \033[32m{min(mencol3)}\033[m')
sleep(2)
mail1 = matriz[0][0], matriz[0][1], matriz[0][2]
mail2 = matriz[1][0], matriz[1][1], matriz[1][2]
mail3 = matriz[2][0], matriz[2][1], matriz[2][2]
print(f'\033[31mO maior  valor da linha\033[m \033[32m1\033[m \033[31mé:\033[m \033[32m{max(mail1)}\033[m')
sleep(2)
print(f'\033[31mO maior  valor da linha\033[m \033[33m2\033[m \033[31mé:\033[m \033[32m{max(mail2)}\033[m')
sleep(2)
print(f'\033[31mO maior  valor da linha\033[m \033[36m3\033[m \033[31mé:\033[m \033[32m{max(mail3)}\033[m')
sleep(2)
menl1 = matriz[0][0], matriz[0][1], matriz[0][2]
menl2 = matriz[1][0], matriz[1][1], matriz[1][2]
menl3 = matriz[2][0], matriz[2][1], matriz[2][2]
print(f'\033[31mO menor  valor da linha\033[m \033[32m1\033[m \033[31mé:\033[m \033[32m{min(menl1)}\033[m')
sleep(2)
print(f'\033[31mO menor  valor da linha\033[m \033[33m2\033[m \033[31mé:\033[m \033[32m{min(menl2)}\033[m')
sleep(2)
print(f'\033[31mO menor  valor da linha\033[m \033[36m3\033[m \033[31mé:\033[m \033[32m{min(menl3)}\033[m')
sleep(2)
somacruz1 = matriz[0][0] + matriz[1][1] + matriz[2][2]
somacruz2 = matriz[0][2] + matriz[1][1] + matriz[2][0]
print(f'''\033[33mA soma da cruzeta, ou seja:
Primeiro valor da  linha\033[m \033[32m1\033[m
\033[33mSegundo  valor da  linha\033[m \033[33m2\033[m
\033[33mTerceiro valor da  linha\033[m \033[36m3\033[m''')
sleep(4)
print(f'\033[31mA soma da cruzeta é:\033[m \033[32m{somacruz1}\033[m')
sleep(2)
print(f'''\033[33mA soma da cruzeta, ou seja:
Terceiro valor da  linha\033[m \033[32m1\033[m
\033[33mSegundo  valor da  linha\033[m \033[33m2\033[m
\033[33mPrimeiro valor da  linha\033[m \033[36m3\033[m''')
sleep(4)
print(f'\033[31mA soma da cruzeta é:\033[m \033[32m{somacruz2}\033[m')
print('\033[31mTodos os valores da matriz são:\033[m')
for l in matriz:
    for c in l:
        print(f'\033[32m{c}\033[m  ', end=''), sleep(1)
        totm = totm + c
print()
sleep(2)
print(f'\033[31mA soma total dos valores da matriz é:\033[m  \033[32m{totm}\033[m')
palavra = 'ACABOU NOSSO PROGRAMA, VOLTE SEMPRE'
for l in palavra:
    print(f'\033[35m{l}\033[m', end=''), sleep(0.4)
print()
sleep(1)
print('Fim...')
