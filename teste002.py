def elevacao(num: int, num1: int):
    cont = 0
    for c in range(0, num1 + 1):
        calc = num ** cont
        print(f'{num} elevado à {cont} = {calc}')
        cont += 1


elevacao(2, 24)
