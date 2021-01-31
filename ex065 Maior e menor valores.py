res = ''
cont = soma = menor = maior = 0
while res != 'N':
    numer = float(input('\033[31mDigite um valor:\033[m '))
    res = str(input('Deseja continuar [s/n]:  ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('Deseja continuar [s/n]:  ')).strip().upper()[0]
    cont = cont + 1
    soma = soma + numer
    if cont == 1:
        menor = numer
        maior = numer
    else:
        if numer < menor:
            menor = numer
        if numer > maior:
            maior = numer
media = soma / cont
print(f'''Você digitou \033[31m{cont}\033[m número(s) e a soma total foi \033[32m{soma:.2f}\033[m
A média de \033[31m{cont}\033[m valor(es) informado(s) ficou em \033[32m{media:.2f}\033[m
Do(s) \033[31m{cont}\033[m valor(es) informado(s) o menor é \033[32m{menor:.2f}\033[m
Do(s) \033[31m{cont}\033[m valor(es) informado(s) o maior é \033[32m{maior:.2f}\033[m''')
