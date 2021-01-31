lista = []
temp = []
while True:
    temp.append(str(input('\033[33mNome do aluno:\033[m  ')).strip().lower().title())
    temp.append(float(input('\033[36m      1ª nota:\033[m  ')))
    temp.append(float(input('\033[36m      2ª nota:\033[m  ')))
    media = (temp[1] + temp[2]) / 2
    temp.append(media)
    lista.append(temp[:])
    temp.clear()
    res = ' '
    while res not in 'SN':
        res = str(input('\033[31m>>>>>>? [S/N]:\033[m  ')).strip().upper()
    if res == 'N':
        break
cont = 1
print('\033[31m=-\033[m' * 28)
print('\033[32mMATRÍCULA\033[m    \033[33mNOME\033[m                             \033[36mMÉDIA\033[m')
print('\033[31m=-\033[m' * 28)
for l in lista:
    print('{:<13}{:<33}{:<5.1f}'.format(cont, l[0], l[3]))
    cont = cont + 1
print()
print('\033[31m=-\033[m' * 28)
while True:
    opcao = int(input('\033[33mDeseja ver as notas de qual aluno? [999 para sair]:\033[m  '))
    while len(lista) < opcao <= 998 or opcao < 1:
        print('\033[31m=-\033[m' * 28)
        opcao = int(input('\033[33mDeseja ver as notas de qual aluno? [999 para sair]:\033[m  '))
    if opcao == 999:
        break
    print('''\033[32mMostrando notas de: {:<15}   \033[m\033[36m{:<5.1f}\033[m    \033[36m{:<5.1f}\033[m'''
          .format(lista[opcao - 1][0], lista[opcao - 1][1], lista[opcao - 1][2]))
    print('\033[31m=-\033[m' * 28)
print('\033[31m=-\033[m' * 28)
print(f'\033[36m{"OBRIGADO, VOLTE SEMPRE":^56}\033[m')
print('\033[31m=-\033[m' * 28)
