lista = list()
dicio = dict()
totidade = 0
while True:
    dicio["Nome"] = str(input('\033[32mInforme o nome:\033[m  ')).strip().lower().title()
    dicio["Sexo"] = str(input('\033[36mInforme o sexo [M/F]:\033[m  ')).strip().upper()
    while dicio["Sexo"] not in 'MF':
        print('\033[31mOPÇÃO INVÁLIDA, POR FAVOR DIGITE APENAS "M" OU "F"\033[m')
        dicio["Sexo"] = str(input('\033[36mInforme o sexo [M/F]:\033[m  ')).strip().upper()
    dicio["Idade"] = int(input('\033[36mInforme a idade:\033[m  '))
    totidade = totidade + dicio["Idade"]
    lista.append(dicio.copy())
    dicio.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]:  ')).strip().upper()
        if resp not in 'SN':
            print('\033[31mOPÇÃO INVÁLIDA, POR FAVOR DIGITE APENAS "S" OU "N"\033[m')
    if resp == 'N':
        break
media = totidade / len(lista)
print('\033[36m--\033[m' * 37)
print(f'\033[32mNo total foram contabilizados:\033[m \033[31m{len(lista)}\033[m \033[32mcadastro(s)\033[m')
print('\033[36m--\033[m' * 37)
print(f'\033[32mA média de idade das pessoas cadastradas é:\033[m \033[31m{media:.2f}\033[m')
print('\033[36m--\033[m' * 37)
print('\033[32mTemos as seguintes pessoas cadastradas do sexo Feminino:\033[m')
print(f'\033[36m{"NOME":<17} {"SEXO":<17} {"IDADE":<18}\033[m')
for d in lista:
    if d["Sexo"] == 'F':
        for v in d.values():
            print('\033[31m{:<18}\033[m'.format(v), end='')
        print()
print('\033[36m--\033[m' * 37)
print('\033[32mSegue abaixo lista das pessoas que estão acima da média de idade do grupo:\033[m')
print(f'\033[36m{"NOME":<17} {"SEXO":<17} {"IDADE":<18}\033[m')
for d in lista:
    if d["Idade"] > media:
        for v in d.values():
            print('\033[31m{:<18}\033[m'.format(v), end='')
        print()
print('\033[36m--\033[m' * 37)
print('\033[33;1mFIM DO PROGRAMA\033[m')
print('\033[36m--\033[m' * 37)
