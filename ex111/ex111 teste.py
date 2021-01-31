from ex111.utilidades import moeda
valor = float(input('Informe um valor:R$  '))
percma = float(input('Informe o percentual (para cima) à ser aplicado: '))
percme = float(input('Informe o percentual (para baixo) à ser aplicado: '))
moeda.resumo(valor, percma, percme)
help(moeda.resumo)
