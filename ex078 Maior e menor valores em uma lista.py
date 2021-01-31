lista = []
maior = menor = cont = 0
for c in range(0, 13):
    numero = int(input(f'Digite um valor para a posição \033[31m{c}\033[m:  '))
    lista.append(numero)
    cont = cont + 1
    if c == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print(f'Sua lista contém os seguintes valores:  ', end='')
for v in lista:
    print(f'\033[32m{v}\033[m  ', end='')
print()
print(f'O maior valor da lista é o número \033[31m{maior}\033[m na(s) posição(ões) ', end='')
for pos, v in enumerate(lista):
    if v == maior:
        print(f'\033[31m[{pos}]  \033[m', end='')
print()
print(f'O menor valor da lista é o número \033[31m{menor}\033[m na(s) posição(ões) ', end='')
for pos, v in enumerate(lista):
    if v == menor:
        print(f'\033[31m[{pos}]  \033[m', end='')
print()
print(f'Sua lista contém \033[31m{cont}\033[m valores')
