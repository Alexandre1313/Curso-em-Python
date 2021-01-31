lis = []
hexa = ''
decimal = 0
cont = 0
while True:
    try:
        lis.clear()
        hexa = str(input('\033[35mDigite o valor em hexadecimal:\033[m  ')).strip().upper()
        for i in hexa:
            if i == 'A':
                lis.append(int(10))
            if i == 'B':
                lis.append(int(11))
            if i == "C":
                lis.append(int(12))
            if i == 'D':
                lis.append(int(13))
            if i == 'E':
                lis.append(int(14))
            if i == 'F':
                lis.append(int(15))
            else:
                if i in '0123456789':
                    lis.append(int(i))
    except(len(lis) != len(hexa)):
        print(end='')
    else:
        if len(lis) == len(hexa) and len(lis) != 0:
            for c in range((len(lis) - 1), -1, -1):
                calculo = (lis[c] * (16 ** cont))
                decimal += calculo
                cont += 1
                print(end='')
            print(f'\033[33mO número\033[m \033[36m{hexa}\033[m \033[33mna base 16 (Hexadecimal) \033[m', end='')
            print(f'\033[33mrepresenta o número\033[m \033[36m{decimal}\033[m \033[33mna base 10 (Decimal)\033[m')
            decimal = 0
            calculo = 0
            cont = 0
            opca = str(input('Deseja realizar outra consulta? [S/N]:  ')).strip().upper()
            while opca not in 'SN':
                opca = str(input('Deseja realizar outra consulta? [S/N]:  ')).strip().upper()
            if opca == 'N':
                break
