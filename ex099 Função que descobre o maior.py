def maior(*num):
    from time import sleep
    mai = menor = 0
    c = 0
    for v in num:
        if c == 0:
            mai = v
            menor = v
            c = c + 1
        else:
            if v > mai:
                mai = v
            if v < menor:
                menor = v
            c = c + 1
    print('\033[36m==\033[m' * 30)
    print('\033[32mForam passados os valores:\033[m  ', end='')
    for i in num:
        if i == mai or i == menor:
            print(f'\033[31m{i}\033[m  ', end='')
            sleep(0.5)
        else:
            print(f'\033[36m{i}\033[m  ', end='')
            sleep(0.5)
    print()
    sleep(1)
    print(f'\033[32mDos valores processados o maior é:\033[m  \033[35m{mai}\033[m')
    sleep(1)
    print(f'\033[32mDos valores processados o menor é:\033[m  \033[35m{menor}\033[m')
    print('\033[36m==\033[m' * 30)


maior(9, 12, 56, 96, 86, 965, 1259, 0, 45, 896, 10259)
maior(3, 6, 9, 5, 45, 96, 753, 1, 36, 123)
maior(96, 45, 2, 62, 12, 99)
maior(10, 11, 12, 15, 96, 1, -123, 639, 599, 499)
maior(5, 9, 4, 8, 7, 9, 75, 42, 46, 91)
