from time import sleep
for c in range(2, 51, 2):
    print(f'\033[32m{c}\033[m  ', end='')
    sleep(0.5)
print()
for c in range(50, 1, -2):
    print(f'\033[31m{c}\033[m  ', end='')
    sleep(0.5)
print()
print('ACABOU!')
