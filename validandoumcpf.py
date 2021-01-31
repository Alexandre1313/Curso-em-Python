original = ''
novocpf = ''
lis = []
dig = []
lis2 = []
while True:
    try:
        lis.clear()
        dig.clear()
        lis2.clear()
        soma1 = soma2 = digito1 = digito2 = 0
        multiplicador1 = multiplicador2 = 2
        novocpf = ''
        original = str(input('Por favor informe seu CPF (Somente números):  '))
        for v in original:
            if v in '0123456789':
                lis.append(int(v))
    except(ValueError, TypeError):
        print('ERRO!!')
    else:
        if len(lis) == len(original) and len(lis) == 11:
            for c in range((len(lis)-3), -1, -1):
                calculo = lis[c] * multiplicador1
                soma1 += calculo
                multiplicador1 += 1
            digito1 = 11 - (soma1 % 11)
            if digito1 > 9:
                digito1 = 0
            dig.append(digito1)
        if len(lis) == len(original) and len(lis) == 11:
            for c in range((len(lis)-2), -1, -1):
                calculo1 = lis[c] * multiplicador2
                soma2 += calculo1
                multiplicador2 += 1
            digito2 = 11 - (soma2 % 11)
            if digito2 > 9:
                digito2 = 0
            dig.append(digito2)
        if len(lis) == len(original) and len(lis) == 11:
            for c in range(len(lis[0:9])):
                lis2.append(str(lis[c]))
            for c in range(len(dig[0:2])):
                lis2.append(str(dig[c]))
            novocpf = ''.join(lis2)
        if len(lis) == len(original) and len(lis) == 11:
            if novocpf == original:
                print(f'\033[32mO CPF\033[m \033[33m{original[0:3]}.{original[3:6]}.{original[6:9]}-', end=''
                      f'{original[9:11]}\033[m \033[32mé um CPF válido!\033[m')
                print()
            else:
                print(f'\033[31mO CPF\033[m \033[33m{original[0:3]}.{original[3:6]}.{original[6:9]}-', end=''
                      f'{original[9:11]}\033[m \033[31m não é um CPF válido!\033[m')
                print()
        else:
            print(f'\033[37mERRO, Informe novamente!\033[m')
