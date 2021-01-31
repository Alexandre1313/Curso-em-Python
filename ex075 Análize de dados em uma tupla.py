tupla = ((int(input('Digite um valor: '))), (int(input('Digite um valor: '))),
         (int(input('Digite um valor: '))), (int(input('Digite um valor: '))),
         (int(input('Digite um valor: '))), (int(input('Digite um valor: '))),
         (int(input('Digite um valor: '))), (int(input('Digite um valor: '))))
print('Sua tupla contém os seguintes valores: ', end='')
for num in tupla:
    if num == 9:
        print(f'\033[35m{num}\033[m  ', end='')
    elif num == 3:
        print(f'\033[33m{num}\033[m  ', end='')
    elif num % 2 == 0:
        print(f'\033[32m{num}\033[m  ', end='')
    else:
        print(f'\033[31m{num}\033[m  ', end='')
print()
cont9 = 0
for c in range(0, 8):
    if tupla[c] == 9:
        cont9 = cont9 + 1
print(f'O número 9 aparece {cont9} vezes dentro da tupla')
if 3 in tupla:
    print(f'A primeira ocorrência do valor 3 foi na posição {tupla.index(3) + 1}')
print('Dos valores informados os pares são: ', end='')
for c in range(0, 8):
    if tupla[c] % 2 == 0:
        print(f'{tupla[c]} ', end='')
