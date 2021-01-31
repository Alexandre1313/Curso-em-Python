print(f'\033[35m{" 10 TERMOS DE UMA PA ":*^40}\033[m')
termo = int(input('Primeiro termo:  '))
razao = int(input('Razão:  '))
dec = termo + (11 - 1) * razao
for n in range(termo, dec, razao):
    print(f'\033[32m{n}\033[m', end=' -> ')
print('ACABOU')

# segundo exemplo

print(f'\033[35m{" 10 TERMOS DE UMA PA ":*^40}\033[m')
termo = int(input('Primeiro termo:  '))
razao = int(input('Razão:  '))
for x in range(1, 11):
    print(f'\033[31m({x}º)\033[m\033[32m[{termo}]\033[m', end='-')
    termo = termo + razao
print('ACABOU')
