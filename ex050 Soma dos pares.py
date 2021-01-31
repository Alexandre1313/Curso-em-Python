soma = cont = 0
for n in range(0, 6):
    numer = int(input(f'Digite o {n + 1}º valor:  '))
    if numer % 2 == 0 and numer != 0:
        soma += numer
        cont += 1
print(f'A soma dos \033[32m{cont}\033[m valores pares digitados foi \033[32m{soma}\033[m')
