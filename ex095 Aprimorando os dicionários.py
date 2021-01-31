def leiaflu(msg):
    ok = False
    valor1 = 0
    while True:
        num1 = str(input(msg))
        if num1.isnumeric():
            valor1 = int(num1)
            ok = True
        elif num1.isspace():
            print(f'\033[33mERRO, você digitou apenas espaços em branco, digite um número inteiro válido\033[m')
        elif num1.isalpha():
            print(f'\033[34mERRO, você digitou apenas letras, digite um número inteiro válido\033[m')
        elif num1.isalnum():
            print(f'\033[35mERRO, você digitou números com letras, digite um número inteiro válido\033[m')
        else:
            print('\033[31mERRO, digite um número inteiro válido!!!\033[m')
        if ok:
            break
    return valor1


# Programa principal

print('\033[36m==\033[m' * 34)
print(f'\033[33;1m{"CADASTRO DE JOGADORES":^68}\033[m')
print('\033[36m==\033[m' * 34)
geral = dict()
lista = list()
lista2 = list()
while True:
    geral['Nome'] = str(input('\033[31mDigite o nome do jogador:\033[m  ')).strip().lower().title()
    partidas = leiaflu(f'\033[31mQuantas partidas\033[m \033[36m{geral["Nome"]}\033[m \033[31mjogou?:\033[m  ')
    for c in range(0, partidas):
        lista.append(leiaflu(f'\033[33mQuantos gols na\033[m \033[36m{c + 1:>4}ª\033[m \033[33mpartida?:\033[m  '))
    geral['Gols'] = lista[:]
    geral['Total'] = sum(lista)
    geral['Media'] = geral["Total"] / len(lista)
    lista.clear()
    lista2.append(geral.copy())
    geral.clear()
    while True:
        res = str(input('Deseja continuar?[S/N]:  ')).strip().upper()
        if res in 'SN':
            break
    if res == 'N':
        break
c = 0
h = 0
print('\033[36m__\033[m' * 34)
print(f'\033[36m{"Nº CADASTRO":<15} {"JOGADOR":<17} {"TOTAL GOLS":<12}      {"GOLS POR PARTIDA"}\033[m')
print('\033[36m__\033[m' * 34)
for d in lista2:
    c = c + 1
    for v in d.values():
        h = h + 1
    print(f'\033[32m{c:<15} {d["Nome"]:<17} {d["Total"]:<18}\033[m', end='')
    for it in d["Gols"]:
        print(f'\033[31m{it}\033[m ', end='')
    print()
print('\033[36m__\033[m' * 34)
while True:
    resp1 = 0
    while len(lista2) < resp1 <= 998 or resp1 < 1:
        resp1 = leiaflu('\033[31mDeseja ve as informações de qual jogador?[999 para finalizar]:\033[m  ')
        if len(lista2) < resp1 <= 998 or resp1 < 1:
            print(F'\033[31mERRO!\033[mNão existe jogador com código {resp1}')
            print('\033[36m__\033[m' * 34)
    if resp1 == 999:
        break
    print(f'\033[36mLevantamento do jogador:\033[m \033[32m{lista2[resp1 - 1]["Nome"]}\033[m')
    w = 1
    for x in lista2[resp1 - 1]["Gols"]:
        print(f'\033[32mNo\033[m \033[36m{w:>3}º\033[m \033[32mjogo fez:', end='')
        print(f'\033[m  \033[36m{x:>4}\033[m \033[32mgols\033[m')
        w = w + 1
    print(f'\033[36m{f"Total gols:":<13}\033[m \033[32m{lista2[resp1 - 1]["Total"]:<15}\033[m', end='')
    print(f'\033[36m{f"Média de gols por partida:":<28}\033[m \033[32m{lista2[resp1 - 1]["Media"]:<7.2f}\033[m')
    print('\033[36m__\033[m' * 34)
print('\033[36m==\033[m' * 34)
print(f'\033[33;1m{"ENCERRADO":^68}\033[m')
print('\033[36m==\033[m' * 34)
print(lista2)
