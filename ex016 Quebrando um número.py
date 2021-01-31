from math import trunc
numer = float(input('Digite um número:  '))
inteiro = trunc(numer)
print(f'Você digitou o número \033[31m{numer}\033[m e sua porção inteira é \033[31m{inteiro:.0f}\033[m')
