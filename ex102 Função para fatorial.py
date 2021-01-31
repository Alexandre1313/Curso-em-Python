def fatorial(num, show=False):
    """
    -> Cálculo de fatorial:
    param num: número do qual deseja ver o fatorial
    param show: opção de ver ou não a conta inteira se True
    return: fatorial de num
    """
    factor = 1
    for c in range(num, 0, -1):
        factor = factor * c
        if show:
            if c != 1:
                print(f'\033[34m{c}\033[m \033[33mx\033[m ', end='')
            else:
                print(f'\033[34m{c}\033[m \033[33m=\033[m ', end='')
    return f'\033[31m{factor}\033[m'


numer = int(input('Digite um número:  '))
print(f'O fatorial de {numer} é {fatorial(numer, True)}')
