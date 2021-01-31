def contador1(i, f, p):
    from time import sleep
    if p < 0:
        p = (p - p * 2)
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(2)
    if i < f:
        c = 0
        cont = i
        while cont <= f:
            if c % 2 == 0:
                print(f'\033[32m{cont:.2f}\033[m ', end='')
                cont = cont + p
                c = c + 1
                sleep(0.5)
            else:
                print(f'\033[33m{cont:.2f}\033[m ', end='')
                cont = cont + p
                c = c + 1
                sleep(0.5)
        print('FIM')
    else:
        c = 0
        cont = i
        while cont >= f:
            if c % 2 == 0:
                print(f'\033[32m{cont:.2f}\033[m ', end='')
                cont = cont - p
                c = c + 1
                sleep(0.5)
            else:
                print(f'\033[33m{cont:.2f}\033[m ', end='')
                cont = cont - p
                c = c + 1
                sleep(0.5)
        print('FIM')


contador1(1, 10, 1)
contador1(10, 0, 2)
contador1(90, 50, 10)
contador1(90, 40, -10)
print('Agora é sua vez de personalizar uma contagem:')
while True:
    ini = float(input('Informe o início:  '))
    fim = float(input('Informe o fim:  '))
    pas = float(input('Informe o passo:  '))
    contador1(ini, fim, pas)
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar?:  ')).strip().upper()
    if res == 'N':
        break
