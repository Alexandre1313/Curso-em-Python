print(f'\033[35m{" LOJAS GUANABARA ":*^40}\033[m')
valor = float(input('Valor da compra:R$  '))
print('''OPÇÕES DE PAGAMENTO:
\033[32m[1] À VISTA (DINHEIRO / CHEQUE)
[2] À VISTA (CARTÃO)
[3] 1 OU 2 X NO CARTÃO
[4] 3 X OU MAIS NO CARTÃO\033[m''')
opcao = int(input('Qual é a sua opção?:  '))
if opcao == 1:
    print('''QUAL SERIA A FORMA DE PAGAMENTO À VISTA:
\033[31m[1] DINHEIRO
[2] CHEQUE\033[m''')
    subop = int(input('Qual é a sua opção?:  '))
    if subop == 1:
        print(f'O valor de sua compra foi de R$ \033[36m{valor:.2f}\033[m')
        print(f'Com desconto de \033[36m15\033[m % para pagamento à vista  em dinheiro  o total à pagar é de', end='')
        print(f' R$ \033[36m{valor - (valor * 15 / 100):.2f}\033[m')
        print(f'Um desconto total de R$ \033[36m{valor - (valor - (valor * 15 / 100)):.2f}\033[m')
    elif subop == 2:
        print(f'O valor de sua compra foi de R$ \033[36m{valor:.2f}\033[m')
        print(f'Com desconto de \033[36m10\033[m % para pagamento à vista no cheque o total à pagar é de', end='')
        print(f' R$ \033[36m{valor - (valor * 10 / 100):.2f}\033[m')
        print(f'Um desconto total de R$ \033[36m{valor - (valor - (valor * 10 / 100)):.2f}\033[m')
    else:
        print('\033[33mOpção inválida, tente novamente\033[m')
elif opcao == 2:
    print(f'O valor de sua compra foi de R$ \033[36m{valor:.2f}\033[m')
    print(f'Com desconto de \033[36m5\033[m % para pagamento à vista no cartão o total à pagar é de', end='')
    print(f' R$ \033[36m{valor - (valor * 5 / 100):.2f}\033[m')
    print(f'Um desconto total de R$ \033[36m{valor - (valor - (valor * 5 / 100)):.2f}\033[m')
elif opcao == 3:
    print(f'''QUAL OPÇÃO DESEJA:
\033[31m[1] 1 X NO CARTÃO
[2] 2 X NO CARTÃO\033[m''')
    subop = int(input('Qual é a sua opção?:  '))
    if subop == 1:
        parc = valor / subop
        print(f'O valor de sua compra foi de R$ \033[36m{valor:.2f}\033[m')
        print(f'Com desconto de \033[36m3\033[m % para pagamento em até \033[36m1\033[m', end='')
        print(f' X no cartão o total à pagar é de', end='')
        print(f' R$ \033[36m{valor - (valor * 3 / 100):.2f}\033[m')
        print(f'Um desconto total de R$ \033[36m{valor - (valor - (valor * 3 / 100)):.2f}\033[m')
    elif subop == 2:
        parc = valor / subop
        print(f'''O valor de sua compra foi de R$ \033[36m{valor:.2f}\033[m
O total à pagar é de \033[36m{subop}\033[m X no cartão de R$ \033[36m{parc:.2f}\033[m sem acréscimo e sem desconto''')
    elif subop != 1 and subop != 2:
        print('\033[33mOpção inválida, tente novamente\033[m')
elif opcao == 4:
    print('''QUAL OPÇÃO DESEJA:
\033[31m[1]  3 X NO CARTÃO
[2]  4 X NO CARTÃO
[3]  5 X NO CARTÃO
[4]  6 X NO CARTÃO
[5]  7 X NO CARTÃO
[6]  8 X NO CARTÃO
[7]  9 X NO CARTÃO
[8] 10 X NO CARTÃO\033[m''')
    subop = int(input('Qual é a sua opção?:  '))
    if 1 <= subop <= 8:
        subop = subop + 2
        valor1 = valor + (valor * 20 / 100)
        parc0 = valor / subop
        parc1 = valor1 / subop
        difer = parc1 - parc0
        print(f'O valor de sua compra foi de R$ \033[36m{valor:.2f}\033[m')
        print(f'Com acréscimo de \033[36m20\033[m % o valor total é de', end='')
        print(f' R$ \033[36m{valor1:.2f}\033[m dividido em', end='')
        print(f' \033[36m{subop}\033[m X de R$ \033[36m{parc1:.2f}\033[m')
        print(f'Um acréscimo total de R$ \033[36m{valor1 - valor:.2f}\033[m')
        print(f'Um acréscimo por parcela de R$ \033[36m{difer:.2f}\033[m')
    else:
        print('\033[33mOpção inválida, tente novamente\033[m')
else:
    print('\033[33mOpção inválida, tente novamente\033[m')
