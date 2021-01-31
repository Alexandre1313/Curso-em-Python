print(f'\033[31m{" GERADOR DE PA ":=^40}\033[m')
primeiro = int(input('Digite o primeiro termo:  '))
razao = int(input('Digite a razão da PA:  '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        if cont % 2 != 0:
            print(f'\033[36m{termo}\033[m \033[33m*\033[m ', end='')
        else:
            print(f'\033[31m{termo}\033[m \033[33m*\033[m ', end='')
        termo = termo + razao
        cont = cont + 1
    print('\033[32mPAUSA\033[m')
    mais = int(input('Quantas PA você quer ver a mais?:  '))
print(f'PROGRESSÃO ARITMÉTICA ENCERRADA COM {total} TERMOS MOSTRADOS')
