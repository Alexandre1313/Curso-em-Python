seg1 = float(input('Medida do primeiro segmento:  '))
seg2 = float(input('Medida do segundo segmento:  '))
seg3 = float(input('Medida do terceiro segmento:  '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos acima PODEM FORMAR TRIÂNGULO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO')
# segundo exemplo
seg1 = float(input('Medida do primeiro segmento:  '))
seg2 = float(input('Medida do segundo segmento:  '))
seg3 = float(input('Medida do terceiro segmento:  '))
lista = [seg1, seg2, seg3]
lista.sort()
if lista[0] + lista[1] > lista[2]:
    print('Os segmentos acima PODEM FORMAR TRIÂNGULO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO')
print(lista)
