lis = []
soma = conta = 0
while True:
    try:
        num = int(input('Informe o valor:  '))
    except (ValueError, TypeError):
        print('ERROR, valor inconsistente!')
    else:
        for cont in range(1, 501, 2):
            if cont % num == 0:
                soma += cont
                conta += 1
            if cont % num == 0:
                lis.append(cont)
                print(cont, end=' ')
        print()
        for i in lis:
            resul = i / num
            if i <= 100:
                print(f'\033[35m{i:<5} / {num:>4} = {resul:.0f}\033[m ')
            if 100 < i < 200:
                print(f'\033[31m{i:<5} / {num:>4} = {resul:.0f}\033[m ')
            if 200 <= i < 300:
                print(f'\033[32m{i:<5} / {num:>4} = {resul:.0f}\033[m ')
            if 300 <= i < 400:
                print(f'\033[33m{i:<5} / {num:>4} = {resul:.0f}\033[m ')
            if 400 <= i < 500:
                print(f'\033[34m{i:<5} / {num:>4} = {resul:.0f}\033[m ')
            if i >= 500:
                print(f'\033[37m{i:<5} / {num:>4} = {resul:.0f}\033[m ')
        print(f'A soma de todos os {conta} valores solicitados é {soma}')
        conta = soma = 0
        lis.clear()
        resp = str(input('Deseja continuar:[S/N]  ')).strip().upper()
        while resp not in 'SN':
            resp = str(input('Deseja continuar:[S/N]  ')).strip().upper()
        if resp == 'N':
            break
print('FIM')
