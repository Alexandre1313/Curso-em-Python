def porcentomais(val=0, perc=0):
    percentual = val * perc / 100
    novoval = val + percentual
    return novoval


def porcentomenos(val=0, perc=0):
    percentual = val * perc / 100
    novoval = val - percentual
    return novoval


def dobro(num=0):
    dobra = num * 2
    return dobra


def metade(num=0):
    metadi = num / 2
    return metadi


def sifrao(preco=0, real='R$'):
    return f'\033[31m{real} {preco:.2f}\033[m'.replace('.', ',')


def percentual(valor=0, perc='%'):
    return f'\033[36m{valor:.2f} {perc}\033[m'.replace('.', ',')
