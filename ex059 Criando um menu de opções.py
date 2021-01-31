from time import sleep
valor1 = float(input('Primeiro valor:  '))
valor2 = float(input('Segundo valor:  '))
opcao = 0
while opcao != 7:
    print('=-'*33)
    print('''\033[32mO que você deseja fazer com esses dois valores:\033[m
\033[33m[1] SOMAR
[2] MULTIPLICAR
[3] SUBTRAIR
[4] DIVIDIR
[5] RAIZ QUADRADA
[6] NOVOS NÚMEROS
[7] SAIR DO PROGRAMA\033[m''')
    opcao = int(input('Escolha uma opção:  '))
    print('=-'*33)
    if opcao == 1:
        soma = valor1 + valor2
        print(f'A soma do valor \033[31m{valor1:.2f}\033[m com o valor ', end='')
        print(f'\033[31m{valor2:.2f}\033[m é igual à \033[32m{soma:.2f}\033[m')
    elif opcao == 2:
        multiplica = valor1 * valor2
        print(f'A multiplicação do valor \033[31m{valor1:.2f}\033[m pelo valor ', end='')
        print(f'\033[31m{valor2:.2f}\033[m é igual à \033[32m{multiplica:.2f}\033[m')
    elif opcao == 3:
        print(f'''\033[32mVocê deseja subtrair :\033[m
\033[33m[1]\033[m \033[31m{valor2}\033[m \033[33mDE\033[m \033[31m{valor1}\033[m
\033[33m[2]\033[m \033[31m{valor1}\033[m \033[33mDE\033[m \033[31m{valor2}\033[m''')
        opcao1 = int(input('Escolha uma opção:  '))
        print('-='*33)
        if opcao1 == 1:
            subtrai = valor1 - valor2
            print(f'A subtração do valor \033[31m{valor2:.2f}\033[m do valor ', end='')
            print(f'\033[31m{valor1:.2f}\033[m é igual à \033[32m{subtrai:.2f}\033[m')
        elif opcao1 == 2:
            subtrai1 = valor2 - valor1
            print(f'A subtração do valor \033[31m{valor1:.2f}\033[m do valor ', end='')
            print(f'\033[31m{valor2:.2f}\033[m é igual à \033[32m{subtrai1:.2f}\033[m')
        else:
            print('Opção inválida!!!')
    elif opcao == 4:
        print(f'''\033[32mVocê deseja dividir:\033[m
\033[33m[1]\033[m \033[31m{valor1}\033[m \033[33mPOR\033[m \033[31m{valor2}\033[m
\033[33m[2]\033[m \033[31m{valor2}\033[m \033[33mPOR\033[m \033[31m{valor1}\033[m''')
        opcao2 = int(input('Escolha uma opção:  '))
        print('=-'*33)
        if opcao2 == 1:
            div = valor1 / valor2
            print(f'A divisão do valor \033[31m{valor1:.2f}\033[m pelo valor ', end='')
            print(f'\033[31m{valor2:.2f}\033[m é igual à \033[32m{div:.2f}\033[m')
        elif opcao2 == 2:
            div1 = valor2 / valor1
            print(f'A divisão do valor \033[31m{valor2:.2f}\033[m pelo valor ', end='')
            print(f'\033[31m{valor1:.2f}\033[m é igual à \033[32m{div1:.2f}\033[m')
        else:
            print('Opção inválida!!!')
    elif opcao == 5:
        print(f'''A raiz quadrada dos valores é:
\033[32m{valor1 ** (1/2)}\033[m para \033[31m{valor1:.2f}\033[m
\033[32m{valor2 ** (1/2)}\033[m para \033[31m{valor2:.2f}\033[m''')
    elif opcao == 6:
        print('Informe os valores novamente:')
        valor1 = float(input('Primeiro valor:  '))
        valor2 = float(input('Segundo valor:  '))
    elif opcao == 7:
        print('FINALIZANDO PROGRAMA...')
    else:
        print('Opção inválida!!!')
sleep(2)
print('OBRIGADO,VOLTE SEMPRE!!!')
