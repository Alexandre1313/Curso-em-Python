while True:
    numer = int(input('De qual valor você deseja ver a tabuada:  '))
    if numer < 0:
        break
    limite = int(input('Digite o limite [0 para padrão até 10]:  '))
    opcao = limite
    if opcao == 0:
        limite = 10
    cont = 1
    if numer % 2 == 0:
        for c in range(1, (limite + 1)):
            print(f'\033[32m{numer:>5}\033[m \033[33mx\033[m \033[32m{cont:<2}\033[m  \033[33m=\033[m', end='')
            print(f' \033[35m{numer * cont:<3}\033[m')
            cont = cont + 1
    else:
        for c in range(1, (limite + 1)):
            print(f'\033[31m{numer:>5}\033[m \033[32mx\033[m \033[31m{cont:<2}\033[m  \033[32m=\033[m', end='')
            print(f' \033[36m{numer * cont:<3}\033[m')
            cont = cont + 1
print('Programa encerrado com sucesso!!!')
