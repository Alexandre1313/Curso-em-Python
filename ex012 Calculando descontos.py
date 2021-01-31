valor = float(input('Qual o valor do produto? R$  '))
perc = float(input('Informe o percentual de desconto: % '))
desconto = valor * perc / 100
print(f'''O produto que custava R$ \033[31m{valor:.2f}\033[m
Com desconto de \033[31m{perc:.2f}\033[m %
Passa a custar R$ \033[31m{valor - desconto:.2f}\033[m''')
valor1 = float(input('Qual o valor do produto: R$  '))
perc1 = float(input('Informe o percentual de acréscimo: %  '))
acres = valor1 * perc1 / 100
print(f'''O produto comprado à R$ \033[31m{valor1:.2f}\033[m
Com um acréscimo de \033[31m{perc1:.2f}\033[m %
Passará à ser comercializado no valor de R$ \033[31m{valor1 + acres:.2f}\033[m''')
