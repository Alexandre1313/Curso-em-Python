geral = []
dados = []
tot = maior = menor = 0
while True:
    dados.append(str(input('Informe seu nome:  ')).strip().lower().title())
    dados.append(float(input('Informe seu peso (Kg):  ')))
    geral.append(dados[:])
    if tot == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    tot = tot + 1
    dados.clear()
    res = ' '
    while res not in "SN":
        res = str(input('Deseja continuar? [S/N]:  ')).strip().upper()
    if res in 'N':
        break
print(f'A(s) pessoa(s) com maior peso (\033[32m{maior:.2f}\033[m kg):  ', end='')
for lis in geral:
    if lis[1] == maior:
        print(f'\033[31m{lis[0]}\033[m  ', end='')
print()
print(f'A(s) pessoa(s) com menor peso (\033[32m{menor:.2f}\033[m kg):  ', end='')
for lis in geral:
    if lis[1] == menor:
        print(f'\033[31m{lis[0]}\033[m  ', end='')
print()
print(f'No total você cadastrou \033[32m{tot}\033[m pessoas')
