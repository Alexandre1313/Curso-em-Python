num = float(input('Digite um número:  '))
num2 = float(input('Digite outro número:  '))
soma = num + num2
soma2 = str(soma)
soma3 = soma2.replace('.', ',')
print(f'A soma do valor {num} mais o valor {num2} é {soma3}')
