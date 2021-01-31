def hexadecimal(*num):
    lista = [*num]
    for v in lista:
        lis = []
        lis2 = []
        lis3 = []
        resul = 16
        operando = v
        while resul >= 16:
            resul = operando / 16
            resto = operando % 16
            operando = resul
            lis.append(int(resto))
            lis2.append(int(resul))
        for k in lis2:
            if k == lis2[-1] and lis2[-1] != 0:
                lis.append(k)
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
        for c in range((len(lis) - 1), -1, -1):
            lis3.append(str(lis[c]))
        valor = ''.join(lis3)
        print(f'\033[35mO número\033[m \033[36m{v:<13}\033[m \033[35mna base decimal(\033[33m10\033[m)\033[m', end=''
              f'\033[35m equivale ao número\033[m \033[36m{valor:<13}\033[m \033[35mna base hexadecimal'
              f'(\033[33m16\033[m).\033[m')
        print()


hexadecimal(1000000000000, 9999999999999)
