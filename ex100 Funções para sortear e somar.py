def sortear(lst):
    """FUNÇÃO SORTEAR
    Sorteia 20 valores e os coloca dentro de uma lista informada como parâmetro
    Números estes sem repetição"""
    from random import randint
    from time import sleep
    cont = 1
    while cont <= 20:
        numer = randint(1, 59)
        if numer not in lst:
            lst.append(numer)
            cont = cont + 1
    for c in range(0, 60):
        print(f'\033[32m-\033[m', end='')
        sleep(0.005)
    print()
    print(f'\033[31mOs valores sorteados foram:\033[m')
    for c in lst:
        if 10 > c >= 0:
            print(f'\033[36m0{c}\033[m ', end='')
            sleep(0.3)
        else:
            print(f'\033[36m{c}\033[m ', end='')
            sleep(0.3)
    print()
    for c in range(0, 60):
        print(f'\033[32m-\033[m', end='')
        sleep(0.005)
    print()


def somapar(lst):
    """FUNÇÃO SOMAPAR
    Recebe uma lista como parâmetro e separa os seus valores
    como par e ímpar, somando as duas classes individualmente no fim da
    execução da função"""
    from time import sleep
    par = im = 0
    for c in range(0, 60):
        print(f'\033[32m-\033[m', end='')
        sleep(0.005)
    print()
    print('\033[31mOs valores pares da lista são:\033[m')
    for c in lst:
        if c % 2 == 0:
            if 10 > c >= 0:
                print(f'\033[36m0{c}\033[m ', end='')
                sleep(0.3)
                par = par + c
            else:
                print(f'\033[36m{c}\033[m ', end='')
                sleep(0.3)
                par = par + c
    print()
    print(f'\033[31mA soma dos valores pares da lista foi:\033[m  \033[33m{par}\033[m')
    for c in range(0, 60):
        print(f'\033[32m-\033[m', end='')
        sleep(0.005)
    print()
    for c in range(0, 60):
        print(f'\033[32m-\033[m', end='')
        sleep(0.005)
    print()
    print('\033[31mOs valores ímpares da lista são:\033[m')
    for c in lst:
        if c % 2 != 0:
            if 10 > c >= 0:
                print(f'\033[36m0{c}\033[m ', end='')
                sleep(0.3)
                im = im + c
            else:
                print(f'\033[36m{c}\033[m ', end='')
                sleep(0.3)
                im = im + c
    print()
    print(f'\033[31mA soma dos valores ímpares da lista foi:\033[m  \033[33m{im}\033[m')
    for c in range(0, 60):
        print(f'\033[32m-\033[m', end='')
        sleep(0.005)
    print()


lista = list()
sortear(lista)
somapar(lista)
lista2 = []
sortear(lista2)
somapar(lista2)
