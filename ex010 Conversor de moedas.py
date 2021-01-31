valor = float(input('Quanto dinheiro você tem na carteira? R$  '))
vdolar = float(input('Digite o valor do dólar do dia: R$  '))
veuro = float(input('Digite o valor do euro do dia: R$  '))
dolar = valor / vdolar
real = dolar * vdolar
euro = valor / veuro
real1 = euro * veuro
print('=-'*30)
print(f'Com o valor de R$ {valor:.2f} você pode comprar U$$ {dolar:.2f}')
print(f'Com U$$ {dolar:.2f} você pode comprar R$ {real:.2f}')
print(f'Com o valor de R$ {valor:.2f} você pode comprar EUR {euro:.2f}')
print(f'Com EUR {euro:.2f} você pode comprar R$ {real1:.2f}')
