import moedas
valor = float(input('Informe um valor:R$  '))
percma = float(input('Informe o percentual (para cima) à ser aplicado: '))
percme = float(input('Informe o percentual (para baixo) à ser aplicado: '))
moedas.resumo(valor, percma, percme)
help(moedas.resumo)
