altura = float(input('Altura [m]:  '))
peso = float(input('Peso [Kg]:  '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'''Seu imc é {imc:.2f}
Você esta ABAIXO DO PESO IDEAL''')
elif 18.5 <= imc < 25:
    print(f'''Seu imc é {imc:.2f}
Você esta NO PESO IDEAL''')
elif 25 <= imc < 30:
    print(f'''Seu imc é {imc:.2f}
Você esta com SOBREPESO''')
elif 30 <= imc < 40:
    print(f'''Seu imc é {imc:.2f}
Você esta com OBESIDADE''')
elif imc >= 40:
    print(f'''Seu imc é {imc:.2f}
Você esta com OBESIDADE MÓRBIDA, cuidado!''')
