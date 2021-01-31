print(f'\033[35m{" 10 TERMOS DE UMA PA ":=^40}\033[m')
termo = int(input('Digite o primeiro termo:  '))
razao = int(input('Digite a razão:  '))
dec = termo + (11 - 1) * razao
while termo < dec:
    print(f'\033[31m{termo}\033[m \033[36m->\033[m ', end='')
    termo = termo + razao
print('\033[32mACABOU\033[m')

# segundo exemplo

print(f'\033[31m{" GERADOR DE PA ":=^40}\033[m')
primeiro = int(input('Digite o primeiro termo:  '))
razao = int(input('Digite a razão da PA:  '))
termo = primeiro
cont = 1
while cont <= 10:
    if cont % 2 != 0:
        print(f'\033[36m{termo}\033[m \033[32m->\033[m ', end='')
    else:
        print(f'\033[31m{termo}\033[m \033[32m->\033[m ', end='')
    termo = termo + razao
    cont = cont + 1
print('\033[32mFIM\033[m')
