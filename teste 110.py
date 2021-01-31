soma = 0
for c in range(1, 5):
    num = float(input(f'Informe o {c}º valor:  '))
    soma = soma + num
media = soma / 4
print(f'A soma dos valores informados é:\033[31m{media:.1f}\033[m')
