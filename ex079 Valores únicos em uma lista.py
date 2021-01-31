lista = []
res = ' '
ont = 0
while True:
    numer = int(input(f'Digite o \033[36m{ont + 1}º\033[m valor:  '))
    if numer not in lista:
        lista.append(numer)
        ont = ont + 1
        print('\033[32mValor adicionado com sucesso!!\033[m')
    else:
        print('\033[31mValor duplicado, não vou adicionar...\033[m')
    res = str(input('Deseja continuar? [S/N]:  ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('\033[33mResposta inválida, deseja continuar? [S/N]:  \033[m')).strip().upper()[0]
    if res == 'N':
        break
ordem = sorted(lista)
print('=-'*55)
print('Os valores de sua lista sem repetições e em ordem crescente foi: ', end='')
for c in range(0, len(ordem)):
    print(f'\033[35m{ordem[c]}\033[m ', end='')
print()
print('=-'*55)
print(f'Sua lista possui \033[31m{ont}\033[m valores ')
print('FIM')
