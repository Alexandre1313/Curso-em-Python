salario = float(input('Salário à ser reajustado:R$  '))
if salario > 2000:
    nsal = (salario * 7 / 100) + salario
    print(f'O valor do salário que é de R$ {salario:.2f} com reajuste de 7% passa a valer R$ {nsal:.2f}')
if 1250 < salario <= 2000:
    nsal = (salario * 10 / 100) + salario
    print(f'O valor do salário que é de R$ {salario:.2f} com reajuste de 10% passa a valer R$ {nsal:.2f}')
if salario <= 1250:
    nsal = (salario * 15 / 100) + salario
    print(f'O valor do salário que é de R$ {salario:.2f} com reajuste de 15% passa a valer R$ {nsal:.2f}')
