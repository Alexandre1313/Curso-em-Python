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
