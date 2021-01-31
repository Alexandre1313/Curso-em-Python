maior = menor = 0
for p in range(1, 6):
    peso = float(input(f'Informe o peso da {p + 1}ª pessoa:Kg  '))
    if p == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'Dos valores informados o maior peso foi {maior} Kg')
print(f'Dos valores informados o menor peso foi {menor} Kg')
