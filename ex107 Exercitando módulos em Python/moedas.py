def porcentomais(val=0, perc=0):
    percentual = val * perc / 100
    novoval = val + percentual
    return f'R$ {novoval:.2f}'


def porcentomenos(val=0, perc=0):
    percentual = val * perc / 100
    novoval = val - percentual
    return f'R$ {novoval:.2f}'


def dobro(num=0):
    dobra = num * 2
    return f'R$ {dobra:.2f}'


def metade(num=0):
    metadi = num / 2
    return f'R$ {metadi:.2f}'
