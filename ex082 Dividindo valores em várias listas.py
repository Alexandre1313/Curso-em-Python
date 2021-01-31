listac = []
listap = []
listai = []
cont = 1
while True:
    numer = int(input(f'Digite o \033[31m{cont}º\033[m valor:  '))
    if numer % 2 == 0:
        listap.append(numer)
        listac.append(numer)
        cont = cont + 1
    else:
        listai.append(numer)
        listac.append(numer)
        cont = cont + 1
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar? [S/N]:  ')).strip().upper()
    if res in 'N':
        break
print('=-'*30)
print(f'A lista completa é: \033[31m{listac}\033[m')
print(f'A lista de números ímpares é: \033[33m{listai}\033[m')
print(f'A lista de números pares é : \033[32m{listap}\033[m')
