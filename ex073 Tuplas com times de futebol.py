times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional',
         'Corinthians', 'Fortaleza EC', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense',
         'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('-'*88)
print(f'Esta é a tabela de classificação do campeonato Brasileiro de futebol, segue informações:')
print('-'*88)
for pos, tim in enumerate(times):
    if pos <= 8:
        print(f'\033[32m0{pos + 1}º colocado: {tim}\033[m')
    else:
        print(f'\033[32m{pos + 1}º colocado: {tim}\033[m')
print('-'*45)
print('Conforme tabela os 5 primeiros colocados são:')
print('-'*45)
for pos, tim in enumerate(times[0:5]):
    if pos <= 8:
        print(f'\033[32m0{pos + 1}º colocado: {tim}\033[m')
print('-'*43)
print('Conforme tabela os 4 últimos colocados são:')
print('-'*43)
for pos, tim in enumerate(times[16:]):
    print(f'\033[32m{pos + 17}º colocado: {tim}\033[m')
print('-'*49)
print('Conforme tabela os times em ordem alfabética são:')
print('-'*49)
for cont in range(0, len(times)):
    print(f'\033[32m{sorted(times)[cont]}\033[m')
print('-'*53)
print('Conforme tabela o time da Chapecoense se encontra na:')
print('-'*53)
for pos, tim in enumerate(times):
    if tim == 'Chapecoense':
        print(f'\033[32m{pos + 1}ª posição\033[m')
print('-'*3)
print('FIM')
print('-'*3)
