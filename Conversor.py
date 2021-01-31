lis = []
binario = ''
decimal = 0
cont = 0
while True:
    try:
        lis.clear()
        binario = str(input('\033[35mDigite o valor em binário:\033[m  '))
        for i in binario:
            if i == '0' or i == '1':
                lis.append(int(i))
    except(len(lis) != len(binario)):
        print(end='')
    else:
        if len(lis) == len(binario) and len(lis) > 1 and lis[0] != 0:
            for c in range((len(lis) - 1), -1, -1):
                calculo = (lis[c] * (2 ** cont))
                decimal += calculo
                cont += 1
                print(end='')
            print(f'\033[33mO número\033[m \033[36m{binario}\033[m \033[33mna base 2 (Binária) \033[m', end='')
            print(f'\033[33mrepresenta o número\033[m \033[36m{decimal}\033[m \033[33mna base 10 (Decimal)\033[m')
            decimal = 0
            calculo = 0
            cont = 0
            opca = str(input('Deseja realizar outra consulta? [S/N]:  ')).strip().upper()
            while opca not in 'SN':
                opca = str(input('Deseja realizar outra consulta? [S/N]:  ')).strip().upper()
            if opca == 'N':
                break
        if len(lis) == len(binario) and len(lis) == 1 and lis[0] == 0:
            for c in range((len(lis) - 1), -1, -1):
                calculo = (lis[c] * (2 ** cont))
                decimal += calculo
                cont += 1
                print(end='')
            print(f'\033[33mO número\033[m \033[36m{binario}\033[m \033[33mna base 2 (Binária) \033[m', end='')
            print(f'\033[33mrepresenta o número\033[m \033[36m{decimal}\033[m \033[33mna base 10 (Decimal)\033[m')
            decimal = 0
            calculo2 = 0
            cont = 0
            opca = str(input('Deseja realizar outra consulta? [S/N]:  ')).strip().upper()
            while opca not in 'SN':
                opca = str(input('Deseja realizar outra consulta? [S/N]:  ')).strip().upper()
            if opca == 'N':
                break
        if len(lis) == len(binario) and len(lis) == 1 and lis[0] == 1:
            for c in range((len(lis) - 1), -1, -1):
                calculo = (lis[c] * (2 ** cont))
                decimal += calculo
                cont += 1
                print(end='')
            print(f'\033[33mO número\033[m \033[36m{binario}\033[m \033[33mna base 2 (Binária) \033[m', end='')
            print(f'\033[33mrepresenta o número\033[m \033[36m{decimal}\033[m \033[33mna base 10 (Decimal)\033[m')
            decimal = 0
            calculo2 = 0
            cont = 0
            opca = str(input('Deseja realizar outra consulta? [S/N]:  ')).strip().upper()
            while opca not in 'SN':
                opca = str(input('Deseja realizar outra consulta? [S/N]:  ')).strip().upper()
            if opca == 'N':
                break
