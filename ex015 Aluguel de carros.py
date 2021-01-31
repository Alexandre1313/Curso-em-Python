dia = int(input('Quantidade de dias de locação:  '))
km = float(input('Quantidade de kilômetros rodados: '))
vd = dia * 60
vk = km * 0.15
print(f'O valor total a pagar é R$ \033[31m{vd + vk:.2f}\033[m')
