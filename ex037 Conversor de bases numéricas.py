opcao = 0
while opcao != 4:
    print('=-' * 29)
    num = int(input('Digite um número inteiro:  '))
    print('=-'*29)
    print('Escolha uma das bases para conversão:')
    print('=-'*29)
    print('''[1] Converter para BINÁRIO
[2] Converter para HEXADECIMAL
[3] Converter para OCTAL
[4] Encerrar programa...''')
    opcao = int(input('Qual é a sua opção?:  '))
    print('=-'*29)
    if opcao == 1:
        print(f'\033[34mO número {num} convertido para base BINÁRIA é:\033[m \033[31m{bin(num)[2:]}\033[m')
    elif opcao == 2:
        print(f'\033[34mO número {num} convertido para base HEXADECIMAL é: {hex(num)[2:]}\033[m')
    elif opcao == 3:
        print(f'\033[34mO número {num} convertido para base OCTAL é: {oct(num)[2:]}\033[m')
    else:
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')
