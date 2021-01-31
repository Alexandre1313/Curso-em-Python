seg1 = float(input('Primeiro segmento:  '))
seg2 = float(input('Segundo segmento:  '))
seg3 = float(input('Terceiro segmento:  '))
trian = [seg1, seg2, seg3]
trian.sort()
if trian[0] + trian[1] > trian[2] and trian[0] == trian[1] == trian[2]:
    print('''Os segmentos acima podem formar um TRIÂNGULO
Um triângulo EQUILÀTERO''')
elif trian[0] + trian[1] > trian[2] and trian[0] == trian[1] != trian[2] or trian[0] != trian[1] == trian[2]:
    print('''Os segmentos acima podem formar um TRIÂNGULO
Um triângulo ISÓSCELES''')
elif trian[0] + trian[1] > trian[2] and trian[0] != trian[1] != trian[2]:
    print('''Os segmentos acima podem formar um TRIÂNGULO
Um triângulo ESCALENO''')
else:
    print('Os segmentos informados NÃO PODEM FORMAR TRIÂNGULO')
