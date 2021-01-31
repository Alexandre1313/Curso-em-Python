salario = float(input('Informe o valor do salário à ser reajustado:R$  '))
percentual = float(input('informe o percentual de reajuste á ser aplicado:  '))
acres = salario * percentual / 100
print(f'O salário de R$ \033[34m{salario:.2f}\033[m com um reajuste de ', end='')
print(f'\033[34m{percentual:.2f}\033[m % tera um aumento de ', end='')
print(f'R$ \033[34m{acres:.2f}\033[m e  passará a valer R$ \033[34m{salario + acres:.2f}\033[m')
print(f'Isso resultará em um montante anual de R$ \033[34m{acres * 13:.2f}\033[m incluindo o 13º salário na soma')
print(f'Resultante num montante anual de salário de R$ \033[34m{(salario + acres) * 13:.2f}\033[m incuimdo 13º salário')
