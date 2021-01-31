sexo = str(input('Digite seu sexo [M/F]:  ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, qual é o seu sexo?[M/F]:  ')).strip().upper()[0]
if sexo == 'M':
    print(f'Sexo {sexo}asculino registrado com sucesso!!')
else:
    print(f'Sexo {sexo}eminino registrado com sucesso!!')
