def area(a, b):
    resul = a * b
    print('\033[36m==\033[m' * 23)
    print(f'\033[36m{f"A área total em m² é:"}\033[33m \033[31m{resul:.2f}\033[m\033[36m{f" m²"}\033[m')
    print('\033[36m==\033[m' * 23)


print('==' * 23)
print(f'{"CONTROLE DE TERRENOS":^46}')
print('==' * 23)
largura = float(input('Digite a largura do terreno [m²]:  '))
comprimento = float(input('Digite o comprimento do terreno [m²]:  '))
area(largura, comprimento)
