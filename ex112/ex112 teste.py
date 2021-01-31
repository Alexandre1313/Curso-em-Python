from ex112.utilidades import moeda
from ex112.utilidades import dado
valor = dado.lerdinheiro('Informe um valor:R$  ')
percma = dado.lerpercentual('Informe o percentual (para cima) à ser aplicado:  ')
percme = dado.lerpercentual('Informe o percentual (para baixo) à ser aplicado:  ')
moeda.resumo(valor, percma, percme)
help(moeda.resumo)
