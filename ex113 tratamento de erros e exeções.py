def leiainteiro(msg):
    while True:
        try:
            num1 = int(input(msg))
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


num = leiainteiro('Digite um valor inteiro:  ')
num2 = leiareal('Digite um valor real:  ')
print(f'O número inteiro informado foi {num} e o número real informado foi {num2}')
