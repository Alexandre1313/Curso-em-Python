geral = dict()
lista = list()
geral['Nome'] = str(input('\033[31mDigite o nome do jogador:\033[m  ')).strip().lower().title()
partidas = int(input(f'\033[31mQuantas partidas\033[m \033[33m{geral["Nome"]}\033[m \033[31mjogou?:\033[m  '))
for c in range(0, partidas):
    lista.append(int(input(f'  \033[33mQuantos gols na\033[m \033[36m{c + 1}ª\033[m \033[33mpartida?:\033[m  ')))
geral['Gols'] = lista[:]
geral['Total'] = sum(lista)
print('\033[32m=-\033[m' * 29)
print(f'\033[36m{geral}\033[m')
print('\033[32m=-\033[m' * 29)
for k, v in geral.items():
    print(f'\033[33;1mO campo\033[m \033[32;1m{k}\033[m \033[33;1mtem o valor\033[m \033[32;1m{v}\033[m')
print('\033[32m=-\033[m' * 29)
print(f'\033[33;1mO jogador\033[m \033[32;1m{geral["Nome"]}\033[m \033[33;1mjogou', end='')
print(f'\033[m \033[32;1m{len(geral["Gols"])}\033[m \033[33;1mpartidas:\033[m')
print('\033[32m=-\033[m' * 29)
for i, v in enumerate(geral["Gols"]):
    print(f'\033[33;1m->->-> Na\033[m\033[36;1m {i + 1}ª\033[m \033[33;1mpartida fez', end='')
    print(f'\033[m \033[32;1m{v}\033[m \033[33;1mgol(s)\033[m')
print('\033[32m=-\033[m' * 29)
print(f'\033[33;1mFoi um total de\033[m \033[32;1m{geral["Total"]}\033[m \033[33;1mgol(s)\033[m')
print('\033[32m=-\033[m' * 29)
print('\033[33;1mFim\033[m')
