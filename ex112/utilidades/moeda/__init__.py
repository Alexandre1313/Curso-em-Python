def porcentomais(val=0, perc=0, formato=True):
    res = val + (val * perc / 100)
    return res if formato is False else sifrao(res)


def porcentomenos(val=0, perc=0, formato=True):
    res = val - (val * perc / 100)
    return res if formato is False else sifrao(res)


def dobro(num=0, formato=True):
    dobra = num * 2
    return dobra if formato is False else sifrao(dobra)


def metade(num=0, formato=True):
    metadi = num / 2
    return metadi if formato is False else sifrao(metadi)


def sifrao(preco=0.0, real='R$'):
    return f'\033[31m{real} {preco:.2f}\033[m'.replace('.', ',')


def percentual(valor=0, perc='%'):
    return f'\033[36m{valor:.2f} {perc}\033[m'.replace('.', ',')


def resumo(valor=0, percmais=0, percmenor=0):
    """
    Função Resumo
    param valor: informe o valor a ser calculado,se nao informado será 0
    param percmais: informe o percentual de aumento que será repassado à 'valor', se não informado será 0
    param percmenor: informe o percentual de desconto que será repassado à 'valor',se nao informado será 0
    também calcula a metade e o dobro de 'valor'
    return: sem retorno
    """
    print('\033[36m=\033[m' * 50)
    print(f'\033[32m{"Resumo do valor":^50}\033[m')
    print('\033[36m=\033[m' * 50)
    print(f'\033[32m{"Valor analizado:":_<37}\033[m{sifrao(valor)}')
    print('\033[36m=\033[m' * 50)
    print(f'\033[32m{"Dobro do valor:":_<37}\033[m{dobro(valor, True)}')
    print(f'\033[32m{"Metade do valor:":_<37}\033[m{metade(valor, True)}')
    print(f'\033[32m{"Valor com":<10}\033[m{percentual(percmais)} \033[32m{"de acréssimo:":_<19}\033[m', end='')
    print(f'{porcentomais(valor, percmais, True)}')
    print(f'\033[32m{"Valor com":<10}\033[m{percentual(percmenor)} \033[32m{"de decréssimo:":_<19}\033[m', end='')
    print(f'{porcentomenos(valor, percmenor, True )}')
    print('\033[36m=\033[m' * 50)


def leiainteiro(msg):
    while True:
        try:
            num1 = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mPor favor, digite um número inteiro válido!!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não informar os dados!!\033[m')
            return 0
        else:
            return num1


def leiareal(msg):

    while True:
        try:
            num1 = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mPor favor, digite um número real válido!!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não informar os dados!!\033[m')
            return 0
        else:
            return num1
