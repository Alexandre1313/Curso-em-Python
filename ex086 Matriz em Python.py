matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'\033[31mDigite um valor para\033[m [\033[31m{l}\033[m, \033[31m{c}\033[m]:  '))
print('\033[31m=-\033[m'*14)
print(f'\033[33m{"MATRIZ PYTHON":^28}\033[m')
print('\033[31m=-\033[m'*14)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'\033[33m[\033[m\033[32m{matriz[l][c]:^7}\033[m\033[33m]\033[m', end='')
    print()
print('\033[31m=-\033[m'*14)
