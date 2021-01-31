soma = cont = 0
while True:
    numer = float(input('Digite um valor [999 para parar]:  '))
    if numer == 999:
        break
    soma = soma + numer
    cont = cont + 1
print(f'''Você informou {cont} valores
E a soma total dos mesmos foi:  {soma}''')
