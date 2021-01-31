lista = []
cont = cont1 = 0
while True:
    numer = int(input(f'Informe o \033[31m{cont + 1}º\033[m número:  '))
    if numer not in lista:
        lista.append(numer)
        cont = cont + 1
        print('\033[32mNúmero adicionado com sucesso!!!\033[m')
    else:
        print('\033[31mNúmero já existente na lista, não adicionado.\033[m')
        cont1 = cont1 + 1
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar? [S/N]:  ')).strip().upper()
    if res == 'N':
        break
lista.sort(reverse=True)
print('=-'*34)
print('Sua lista do maior para o menor se compõe como segue:  ', end='')
for c in range(0, len(lista)):
    print(f'\033[31m{lista[c]}\033[m ', end='')
print()
print(f'''Você informou ao todo \033[31m{cont1 + cont}\033[m valores
Dos quais \033[31m{cont}\033[m foram válidos e entraram na lista''')
if cont1 > 0:
    print(f'E \033[31m{cont1}\033[m foram valores repetidos e por isso não foram adicionados à lista')
if 5 in lista:
    print('\033[32mO valor\033[m \033[31m5\033[m \033[32mfaz parte da lista\033[m')
else:
    print('\033[31mO valor\033[m \033[32m5\033[m \033[31mnão foi encontrado na lista\033[m')
print('=-'*34)
