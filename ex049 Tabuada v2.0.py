from time import sleep
numer = float(input('Digite um número para ver sua tabuada:  '))
numer2 = int(input('Digite o limite do cálculo [ex: até 50]:  '))
print('-'*32)
for m in range(1, numer2 + 1):
    print(f'\033[31m{numer:.2f}\033[m x \033[32m{m:.2f}\033[m = \033[33m{numer * m:.2f}\033[m')
    sleep(0.001)
print('FIM')
