from datetime import datetime
anoatual = datetime.now().year
ficha = []
dados = dict()
while True:
    dados['Nome'] = str(input('\033[31mDigite o nome:\033[m  ')).strip().lower().title()
    dados['Nascimento'] = int(input('\033[36mDigite o ano de nascimento:\033[m  '))
    if anoatual - dados['Nascimento'] >= 16:
        while dados['Nascimento'] > anoatual:
            dados['Nascimento'] = int(input('\033[36mDigite o ano de nascimento:\033[m  '))
        dados['CTPS'] = int(input('\033[36mCarteira de trabalho CTPS [0 = não possui]:\033[m  '))
        while dados['CTPS'] < 0:
            dados['CTPS'] = int(input('\033[36mCarteira de trabalho [0 = não possui]:\033[m  '))
        if dados['CTPS'] == 0:
            ficha.append(dados.copy())
            dados.clear()
        elif dados["CTPS"] > 0:
            dados['Ano'] = int(input('\033[36m1º Ano de contratação:\033[m  '))
            while dados['Ano'] < dados['Nascimento'] + 16:
                print('\033[33mTrabalhador nao pode ter sido registrado nesse ano, pois é menor de idade\033[m')
                dados['Ano'] = int(input('\033[36m1º Ano de contratação:\033[m  '))
            dados['Salário'] = float(input('\033[36mInforme o salário:R$\033[m  '))
            ficha.append(dados.copy())
            dados.clear()
    else:
        print('\033[33mEsse trabalhador que deseja cadastrar ainda não pode ter trabalhado, \033[m', end='')
        print('\033[33mpois é menor de 16 anos\033[m')
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar? [S/N]:  ')).strip().upper()
    if res == 'N':
        break
c = 1
print('\033[31m=-\033[m' * 37)
print(f'\033[31m{"Nº CADASTRO":<13} {"CTPS":<10} {"TRABALHADOR":<27}\033[m')
print('\033[31m=-\033[m' * 37)
for d in ficha:
    print(f'{c:<13} {d["CTPS"]:<10} {d["Nome"]:<27}')
    c = c + 1
print('\033[31m=-\033[m' * 37)
while True:
    resp1 = 0
    while len(ficha) < resp1 <= 998 or resp1 < 1:
        resp1 = int(input('De qual trabalhador deseja saber mais informações?[999 para sair]:  '))
    if resp1 == 999:
        break
    for c in range(0, 1):
        idade = anoatual - ficha[resp1 - 1]["Nascimento"]
        if ficha[resp1 - 1]["CTPS"] == 0 and idade >= 16:
            idade = anoatual - ficha[resp1 - 1]["Nascimento"]
            print(f'''\033[33;4;1mVocê optou em ver as informações do trabalhador:\033[m
Nome : \033[32m{ficha[resp1 - 1]["Nome"]}\033[m
Idade: \033[32m{idade}\033[m
CTPS : \033[32m{ficha[resp1 - 1]["CTPS"]}\033[m''')
            print('\033[31m=-\033[m' * 37)
        elif ficha[resp1 - 1]["CTPS"] > 0 and idade >= 16:
            anoap = ficha[resp1 - 1]["Ano"] + 35
            idadecome = ficha[resp1 - 1]["Ano"] - ficha[resp1 - 1]["Nascimento"]
            idadeap = idadecome + 35
            print(f'''\033[33;4;1mVocê optou em ver as informações do trabalhador:\033[m
Nome                           : \033[32m{ficha[resp1 - 1]["Nome"]}\033[m
Idade                          : \033[32m{idade}\033[m
CTPS                           : \033[32m{ficha[resp1 - 1]["CTPS"]}\033[m
1º ano de registro na CTPS     : \033[32m{ficha[resp1 - 1]["Ano"]}\033[m
Salário                        : \033[32mR$ {ficha[resp1 - 1]["Salário"]:.2f}\033[m
Ano da provável aposentadoria  : \033[32m{anoap}\033[m
Idade da provável aposentadoria: \033[32m{idadeap}\033[m''')
            print('\033[31m=-\033[m' * 37)
print('\033[31m=-\033[m' * 37)
print('\033[33;1mPrograma finalizado com sucesso!!!\033[m')
print('\033[31m=-\033[m' * 37)
print('\033[33;1mFIM\033[m')
