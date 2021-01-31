n1 = int(input('Primeiro número:  '))
n2 = int(input('Segundo número:  '))
if n1 > n2:
    print('\033[33mO primeiro número é MAIOR\033[m')
elif n2 > n1:
    print('\033[32mO segundo número é MAIOR\033[m')
else:
    print('\033[31mOs dois números são IGUAIS\033[m')
