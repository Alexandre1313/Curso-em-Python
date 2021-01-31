def jogador(nome='\033[31m<desconhecido>\033[m', gol=0):
    if gol == 1:
        print(f'\033[36mO jogador\033[m \033[31m{nome}\033[m \033[36mfez \033[m', end='')
        print(f'\033[31m{gol}\033[m \033[36mgol no campeonato\033[m')
    else:
        print(f'\033[36mO jogador\033[m \033[31m{nome}\033[m \033[36mfez \033[m', end='')
        print(f'\033[31m{gol}\033[m \033[36mgols no campeonato\033[m')


jog = str(input('\033[34mInforme o nome do jogador:\033[m  ')).strip().lower().title()
go = str(input('\033[34mInforme a quantidade de gols:\033[m  '))
if go.isnumeric():
    go = int(go)
else:
    go = 0
if jog == '':
    jogador(gol=go)
else:
    jogador(jog, go)
