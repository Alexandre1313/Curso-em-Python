veloc = float(input('Digite a velocidade do veículo:  '))
if veloc <= 80:
    print('Tenha um bom dia, dirija com segurança!!!')
else:
    base = (veloc - 80) * 7
    print(f'''Dirija com mais atenção!!
Você foi multado em R$ {base:.2f}''')
