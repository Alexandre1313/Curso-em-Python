from math import hypot
co = float(input('Comprimento do cateto oposto:  '))
ca = float(input('Comprimento do cateto adjacente:  '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')
co1 = float(input('Comprimento do cateto oposto:  '))
ca1 = float(input('Comprimento do cateto adjacente:  '))
hi1 = hypot(co1, ca1)
print(f'A hipotenusa vai medir {hi1:.2f}')
