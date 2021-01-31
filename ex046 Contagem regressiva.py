from time import sleep
for c in range(10, -1, -1):
    print(f'\033[33m{c}\033[m ', end='')
    sleep(1)
print()
for c in range(0, 11):
    print('\033[33mBUM\033[m ', end='')
    sleep(0.7)
    print('\033[31mPOW\033[m ', end='')
    sleep(0.7)
