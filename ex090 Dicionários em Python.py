dados = dict()
ficha = list()
while True:
    dados['Nome'] = str(input('\033[31mDigite o nome do aluno:\033[m  ')).strip().lower().title()
    dados['Nota1'] = float(input('\033[33mInforme a 1ª nota:\033[m  '))
    dados['Nota2'] = float(input('\033[33mInforme a 2ª nota:\033[m  '))
    dados['Nota3'] = float(input('\033[33mInforme a 3ª nota:\033[m  '))
    media = (dados['Nota1'] + dados['Nota2'] + dados['Nota3']) / 3
    dados['Média'] = media
    ficha.append(dados.copy())
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar? [S/N]:  ')).strip().upper()
    if res == 'N':
        break
print(f'\033[31m{"=-" * 29}\033[m')
print(f'\033[31m{"Nº cadastro":<27} {"Nome do aluno":<27}\033[m')
print(f'\033[31m{"=-" * 29}\033[m')
c = 1
for d in ficha:
    print(f'\033[33m{c:<27} {d["Nome"]:<27}\033[m')
    c = c + 1
print(f'\033[31m{"=-" * 29}\033[m')
while True:
    resp = 0
    while len(ficha) < resp <= 998 or resp < 1:
        resp = int(input('Deseja ver a situação de qual aluno? [999 para sair]:  '))
        print(f'\033[31m{"=-" * 29}\033[m')
    if resp == 999:
        break
    for c in range(0, 1):
        if ficha[resp - 1]["Média"] >= 7:
            print(f'\033[31m{"Você optou por ver a situação do aluno:":^58}\033[m')
            print(f'\033[31m{"=-" * 29}\033[m')
            print(f'''\033[31mNome    :\033[33m {ficha[resp - 1]["Nome"]}\033[m
\033[31mNota 1  :\033[m \033[33m{ficha[resp - 1]["Nota1"]}\033[m
\033[31mNota 2  :\033[m \033[33m{ficha[resp - 1]["Nota2"]}\033[m
\033[31mNota 3  :\033[m \033[33m{ficha[resp - 1]["Nota3"]}\033[m
\033[31mMédia   :\033[m \033[32m{ficha[resp - 1]["Média"]:.1f}\033[m
\033[31mSituação:\033[m \033[32mAPROVADO\033[m''')
        elif 7 > ficha[resp - 1]["Média"] >= 5:
            print(f'\033[31m{"Você optou por ver a situação do aluno:":^58}\033[m')
            print(f'\033[31m{"=-" * 29}\033[m')
            print(f'''\033[31mNome    :\033[33m {ficha[resp - 1]["Nome"]}\033[m
\033[31mNota 1  :\033[m \033[33m{ficha[resp - 1]["Nota1"]}\033[m
\033[31mNota 2  :\033[m \033[33m{ficha[resp - 1]["Nota2"]}\033[m
\033[31mNota 3  :\033[m \033[33m{ficha[resp - 1]["Nota3"]}\033[m
\033[31mMédia   :\033[m \033[33m{ficha[resp - 1]["Média"]:.1f}\033[m
\033[31mSituação:\033[m \033[33mEM RECUPERAÇÃO\033[m''')
        elif ficha[resp - 1]["Média"] < 5:
            print(f'\033[31m{"Você optou por ver a situação do aluno:":^58}\033[m')
            print(f'\033[31m{"=-" * 29}\033[m')
            print(f'''\033[31mNome    :\033[33m {ficha[resp - 1]["Nome"]}\033[m
\033[31mNota 1  :\033[m \033[33m{ficha[resp - 1]["Nota1"]}\033[m
\033[31mNota 2  :\033[m \033[33m{ficha[resp - 1]["Nota2"]}\033[m
\033[31mNota 3  :\033[m \033[33m{ficha[resp - 1]["Nota3"]}\033[m
\033[31mMédia   :\033[m \033[31m{ficha[resp - 1]["Média"]:.1f}\033[m
\033[31mSituação:\033[m \033[31mREPROVADO\033[m''')
print(f'\033[33m{"Programa finalizado com sucesso!!!":^58}\033[m')
print(f'\033[31m{"=-" * 29}\033[m')
