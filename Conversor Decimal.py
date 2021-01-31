lis = []
lis2 = []
while True:
    try:
        lis.clear()
        lis2.clear()
        resto = 0
        resul = 16
        decimal = int(input('\033[35mDigite o valor em decimal:\033[m  '))
        operando = decimal
        while resul >= 16:
            resul = operando / 16
            resto = operando % 16
            operando = resul
            lis.append(int(resto))
            lis2.append(int(resul))
    except(TypeError, ValueError):
        print('Digite um número inteiro válido')
    else:
        for v in lis2:
            if v == lis2[-1] and lis2[-1] != 0:
                lis.append(v)
        for c in range((len(lis) - 1), -1, -1):
            if lis[c] == 10:
                lis[c] = 'A'
            if lis[c] == 11:
                lis[c] = 'B'
            if lis[c] == 12:
                lis[c] = 'C'
            if lis[c] == 13:
                lis[c] = 'D'
            if lis[c] == 14:
                lis[c] = 'E'
            if lis[c] == 15:
                lis[c] = 'F'
        print(f'\033[33mO número\033[m \033[36m{decimal}\033[m \033[33mna base 10 (Decimal) ', end='')
        print(f'\033[33mcorresponde ao número\033[m ', end='')
        for t in range((len(lis) - 1), -1, -1):
            print(f'\033[36m{lis[t]}\033[m', end='')
        print(f' \033[33mna base 16 (Hexadecimal).\033[m')
        cont = str(input('Deseja continuar? [S/N]:  ')).strip().upper()
        while cont not in 'SN':
            cont = str(input('Deseja continuar? [S/N]:  ')).strip().upper()
        if cont == 'N':
            break
print(lis)
print(lis2)
