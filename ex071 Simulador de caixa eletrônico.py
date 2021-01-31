print('='*44)
print(f'{"BANCO CEV":^40}')
print('='*44)
total = int(input('Qual o valor do saque? R$ '))
valor = total
cedula = 50
totcedula = 0
while True:
    if valor >= cedula:
        valor = valor - cedula
        totcedula = totcedula + 1
    else:
        if totcedula > 0:
            print(f'Total de \033[32m{totcedula}\033[m cédula(s) de R$ \033[31m{cedula}\033[m')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        totcedula = 0
        if valor == 0:
            break
print('='*44)
print('Volte sempre ao banco CEV, tenha um bom dia!')
