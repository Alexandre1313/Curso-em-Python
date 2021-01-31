def juros(valor: float, perc: float, par: int):
    soma0 = valor
    for c in range(1, par + 1):
        calculo = valor * perc / 100
        soma0 += calculo
        valor = soma0
        print(f'No {c:>3}º mês sua divida é:R$ {soma0:>9.2f}, valor parcela atual R${soma0 / par:>9.2f}')
    return soma0 / par


def juros2(valor=float(), perc=float(), par=int()):
    soma0 = 0
    for c in range(1, par + 1):
        calculo = valor * perc / 100
        soma0 += calculo
    valor += soma0
    print(f'{soma0:>9.2f}')
    return valor / par


def juros3(valor: float, perc: float, par: int):
    soma0 = 0
    parcela = par
    percentual = perc
    while parcela > 0:
        calculo = valor * percentual / 100
        soma0 += calculo
        valor += calculo
        parcela -= 1
        print(f'{soma0:.2f}')
    return valor / par, par


valore = float(input('Informe o valor do empréstimo:R$  '))
meses = int(input('Informe o prazo para pagamento (em meses):  '))
vari = juros(valore, 1, meses)
print(f'Gerando em {meses:>3} meses uma parcela de : parcela final R$\033[33m{vari:>9.2f}\033[m')
