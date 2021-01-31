def lerdinheiro(msg):
    ok = False
    num = 0
    while not ok:
        num = str(input(msg)).replace(',', '.').strip()
        if num.isnumeric():
            ok = True
        elif num.isalpha() or num == '':
            print(f'\033[31mERRO! \"{num}\" não é um valor válido.\033[m')
        elif num.isalnum():
            print(f'\033[31mERRO! \"{num}\" não é um valor válido.\033[m')
        else:
            ok = True
    return float(num)


def lerpercentual(msg):
    ok = False
    num = 0
    while not ok:
        num = str(input(msg)).replace(',', '.').strip()
        if num.isnumeric():
            ok = True
        elif num.isalpha() or num == '':
            print(f'\033[31mERRO! \"{num}\" não é um valor válido.\033[m')
        elif num.isalnum():
            print(f'\033[31mERRO! \"{num}\" não é um valor válido.\033[m')
        else:
            ok = True
    return float(num)
