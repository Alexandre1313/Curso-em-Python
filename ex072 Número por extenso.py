contador = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE',
            'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE',
            'VINTE UM', 'VINTE DOIS', 'VINTE TRÊS')
while True:
    numero = int(input('Qual número você quer que eu escreva por extenso? [0 à 23]:  '))
    if numero > 23 or numero < 0:
        break
    if numero % 2 == 0:
        print(f'\033[32mVocê digitou o número\033[m \033[31;1m[ \033[m', end='')
        print(f'\033[33;1m{contador[numero]} \033[m\033[31;1m]\033[m')
    else:
        print(f'\033[33mVocê digitou o número\033[m \033[31;1m[ \033[m', end='')
        print(f'\033[32;1m{contador[numero]} \033[m\033[31;1m]\033[m')
print('\033[31mOpção inválida!\033[m')
print('Fim do programa')
