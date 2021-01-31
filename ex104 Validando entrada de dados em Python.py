def leiaint(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[31mERRO,digite um número inteiro válido!!!\033[m')
        if ok:
            break
    return valor


def leiaflu(msg):
    ok = False
    valor1 = 0
    while True:
        num1 = str(input(msg))
        if num1.isnumeric():
            valor1 = int(num1)
            ok = True
        elif num1.isspace():
            print(f'\033[33mERRO, você digitou apenas espaços em branco, digite um número inteiro válido\033[m')
        elif num1.isalpha():
            print(f'\033[34mERRO, você digitou apenas letras, digite um número inteiro válido\033[m')
        elif num1.isalnum():
            print(f'\033[35mERRO, você digitou números com letras, digite um número inteiro válido\033[m')
        else:
            print('\033[31mERRO, digite um número inteiro válido!!!\033[m')
        if ok:
            break
    return valor1


n = leiaint('Digite um número:  ')
print(f'\033[32mVocê digitou o número\033[m \033[33m{n}\033[m')
namber = leiaflu('Digite um número: ')
print(f'\033[32mVocê digitou o número\033[m \033[33m{namber}\033[m')
