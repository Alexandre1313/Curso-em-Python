viagem = float(input('Distância da viagem em KM:  '))
if viagem <= 200:
    caro = viagem * 0.50
    print(f'O custo da sua viagem de {viagem} KM será de R$ {caro:.2f}')
else:
    barato = viagem * 0.45
    print(f'O custo da sua viagem de {viagem} Km será de R$ {barato:.2f}')
