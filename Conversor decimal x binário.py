lis = []
lis2 = []
while True:
    resto = 1
    try:
        lis.clear()
        lis2.clear()
        decimal = int(input('Informe o valor à ser convertido para base 2:  '))
        operando = decimal
    except(ValueError, TypeError):
        print(f'Valor inválido!!!')
    else:
        while operando > 0:
            resul = operando // 2
            resto = operando % 2
            operando = resul
            lis.append(int(resto))

        print(lis)
        print(lis2)
