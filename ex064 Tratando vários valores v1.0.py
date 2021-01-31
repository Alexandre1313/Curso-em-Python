numer = cont = total = 0
while numer != 999:
    numer = float(input('Digite um número [999 para parar]:  '))
    if numer != 999:
        total = total + numer
        cont = cont + 1
print(f'A soma dos {cont} valores informados é {total:.2f}')
