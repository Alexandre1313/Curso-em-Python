def leiainteiro(msg):
    while True:
        try:
            num1 = int(input(f'\033[31m{msg}\033[m'))
        except (ValueError, TypeError):
            print('\033[31mPor favor, digite um número inteiro válido!!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não informar os dados!!\033[m')
            return 0
        else:
            return num1


def leiareal(msg):

    while True:
        try:
            num1 = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mPor favor, digite um número real válido!!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não informar os dados!!\033[m')
            return 0
        else:
            return num1


def linha(tam=72):
    return '\033[36m=\033[m' * tam


def cabecalho(txt):
    print(linha())
    print(f'\033[32m{txt.center(72)}\033[m')
    print(linha())


def menu(lista):
    cabecalho('Menu principal')
    c = 1
    for item in lista:
        print(f'\033[33mOpção {c}\033[m - \033[34m{item}\033[m')
        c = c + 1
    print(linha())
    opc = leiainteiro('Sua opção:  ')
    return opc
