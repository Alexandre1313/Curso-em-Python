quant = int(input('Quantos termos da sequência de FIBONACCI deseja visualizar:  '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2} -> ', end='')
cont = 3
mais = quant
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        t3 = t1 + t2
        print(f'{t3} -> ', end='')
        t1 = t2
        t2 = t3
        cont = cont + 1
    print('pausa...')
    mais = int(input('Quantas sequências quer visualizar a mais:  '))
print(f'Sequência de FIBONACCI encerrada com {total} termos apresentados na tela')
