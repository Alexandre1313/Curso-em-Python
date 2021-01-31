lista = []
dados = []
soma1 = soma = 0
setenta = 7.0
arred = 6.52
setenta1 = 70.0
arred1 = 65.20
nota = 0
print('\033[32m==\033[m' * 41)
print(f'\033[36;41m{"Cálculo de média das matérias":^82}\033[m')
print('\033[32m==\033[m' * 41)
for c in range(1, 5):
    while True:
        try:
            nota = float(input(f'\033[34mInforme a \033[m\033[32m{c}ª\033[m \033[34mnota:\033[m  '))
            while nota < 0 or nota > 10:
                print('\033[31mERRO!!!A nota obrigatoriamente tem de ser entre 0 e 10, informe novamente\033[m')
                nota = float(input(f'\033[34mInforme a \033[m\033[32m{c}ª\033[m \033[34mnota:\033[m  '))
        except (ValueError, TypeError):
            print('\033[31mERRO!!!A nota obrigatoriamente tem de ser entre 0 e 10, informe novamente\033[m')
        else:
            if c == 1:
                media1 = nota * 1.50 / 10
                media11 = nota * 1.50
                soma = soma + media1
                soma1 = soma1 + media11
                setenta = setenta - media1
                arred = arred - media1
                setenta1 = setenta1 - media11
                arred1 = arred1 - media11
                dados.append(nota)
                dados.append(media1)
                dados.append(media11)
                lista.append(dados[:])
                dados.clear()
            if c == 2:
                media2 = nota * 1.50 / 10
                media21 = nota * 1.50
                soma = soma + media2
                soma1 = soma1 + media21
                setenta = setenta - media2
                arred = arred - media2
                setenta1 = setenta1 - media21
                arred1 = arred1 - media21
                dados.append(nota)
                dados.append(media2)
                dados.append(media21)
                lista.append(dados[:])
                dados.clear()
            if c == 3:
                media3 = nota * 3 / 10
                media31 = nota * 3
                soma = soma + media3
                soma1 = soma1 + media31
                setenta = setenta - media3
                arred = arred - media3
                setenta1 = setenta1 - media31
                arred1 = arred1 - media31
                dados.append(nota)
                dados.append(media3)
                dados.append(media31)
                lista.append(dados[:])
                dados.clear()
            if c == 4:
                media4 = nota * 4 / 10
                media41 = nota * 4
                soma = soma + media4
                soma1 = soma1 + media41
                setenta = setenta - media4
                arred = arred - media4
                setenta1 = setenta1 - media41
                arred1 = arred1 - media41
                dados.append(nota)
                dados.append(media4)
                dados.append(media41)
                lista.append(dados[:])
                dados.clear()
            break
cont = 1
print('\033[32m==\033[m' * 41)
print(f'\033[36;41m{"            Nota"}{"Média da nota":>29}{"Total pontos da nota":>37}\033[m')
print('\033[32m==\033[m' * 41)
for lis in lista:
    print(f'\033[33m{cont}ª prova:\033[m   \033[35m{lis[0]:<20.1f}\033[m\033[32m{lis[1]:<29.3f} {lis[2]:<29.3f}\033[m')
    cont = cont + 1
print('\033[32m==\033[m' * 41)
if soma <= 10:
    print(f'\033[36;41m{"Informações gerais":^82}\033[m')
    print('\033[32m==\033[m' * 41)
    print(f'\033[34m{"Média à ser atingida:":<67}\033[m\033[32m{"7.0"}\033[m')
    print(f'\033[34m{"Percentual já conquistado  em relação à média 7.0:":<67}\033[m', end='')
    print(f'\033[35m{soma * 100 / 7:.1f} %\033[m')
    print(f'\033[34m{"Percentual já conquistado  em relação a média por arredondamento:":<67}\033[m', end='')
    print(f'\033[35m{soma * 100 / 6.52:.1f} %\033[m')
    print(f'\033[34m{"Percentual já conquistado  em relação ao curso:":<67}\033[m', end='')
    print(f'\033[35m{soma * 100 / 10:.1f} %\033[m')
    perc = setenta * 100 / 10
    if perc > 0:
        print(f'\033[34m{"Percentual faltante em relação ao curso:":<67}\033[m', end='')
        print(f'\033[35m{perc:.1f} %\033[m')
    if perc == 0:
        print(f'\033[34m{"Não houve sobras nem falta nesse percentual em relação ao curso:":<67}\033[m', end='')
        print(f'\033[33m{perc:.1f} %\033[m')
    if perc < 0:
        print(f'\033[34m{"Percentual conquistado à mais em relação ao curso/média:":<67}\033[m', end='')
        print(f'\033[32m{perc - perc * 2:.1f} %\033[m')
    if soma >= 7:
        print(f'\033[34m{"Média conquistada até o momento:":<67}\033[m', end='')
        print(f'\033[32m{soma:<5.3f}\033[m')
    if soma < 7:
        print(f'\033[34m{"Média conquistada até o momento:":<67}\033[m', end='')
        if soma < 6.52:
            print(f'\033[31m{soma:.3f}\033[m')
        elif 6.52 <= soma < 7:
            print(f'\033[33m{soma:.3f}\033[m')
        if setenta > 0:
            print(f'\033[34m{"Falta para atingir a média:":<67}\033[m\033[31m{setenta:.3f}\033[m')
        if arred > 0:
            print(f'\033[34m{"Falta para atingir a média por arredondamento:":<67}\033[m\033[31m{arred:.3f}\033[m')
        if setenta > 0:
            print(f'\033[34m{"Percentual faltante para atingir a média:":<67}\033[m', end='')
            print(f'\033[35m{setenta * 100 / 7:.1f} %\033[m')
        if arred > 0:
            print(f'\033[34m{"Percentual faltante para atingir a média por arredondamento:":<67}\033[m', end='')
            print(f'\033[35m{arred * 100 / 6.52:.1f} %\033[m')
    if lista[0][0] == 0 and lista[1][0] > 0 and lista[2][0] > 0 and lista[3][0] > 0:
        notapf = setenta * 10 / 1.5
        notaar = arred * 10 / 1.5
        if 0 < notapf <= 10:
            print(f'\033[34mVocê terá que tirar\033[m \033[32m{notapf:.1f}\033[m \033[34mna prova\033[m', end='')
            print(f'\033[32m 1\033[m \033[34mpara ser aprovado\033[m')
        if 0 < notaar <= 10:
            print(f'\033[33mVocê terá que tirar\033[m \033[35m{notaar:.1f}\033[m \033[33mna prova\033[m', end='')
            print(f'\033[35m 1\033[m \033[33mpara ser aprovado por arredondamento de média\033[m')
        if notapf <= 0:
            print('\033[32mJá aprovado!!\033[m')
        if notaar > 10:
            print('\033[31mJá reprovado!!\033[m')
    if lista[1][0] == 0 and lista[0][0] > 0 and lista[2][0] > 0 and lista[3][0] > 0:
        notapf = setenta * 10 / 1.5
        notaar = arred * 10 / 1.5
        if 0 < notapf <= 10:
            print(f'\033[34mVocê terá que tirar\033[m \033[32m{notapf:.1f}\033[m \033[34mna prova\033[m', end='')
            print(f'\033[32m 2\033[m \033[34mpara ser aprovado\033[m')
        if 0 < notaar <= 10:
            print(f'\033[33mVocê terá que tirar\033[m \033[35m{notaar:.1f}\033[m \033[33mna prova\033[m', end='')
            print(f'\033[35m 2\033[m \033[33mpara ser aprovado por arredondamento de média\033[m')
        if notapf <= 0:
            print('\033[32mJá aprovado!!\033[m')
        if notaar > 10:
            print('\033[31mJá reprovado!!\033[m')
    if lista[2][0] == 0 and lista[0][0] > 0 and lista[1][0] > 0 and lista[3][0] > 0:
        notapf = setenta * 10 / 3.0
        notaar = arred * 10 / 3.0
        if 0 < notapf <= 10:
            print(f'\033[34mVocê terá que tirar\033[m \033[32m{notapf:.1f}\033[m \033[34mna prova\033[m', end='')
            print(f'\033[32m 3\033[m \033[34mpara ser aprovado\033[m')
        if 0 < notaar <= 10:
            print(f'\033[33mVocê terá que tirar\033[m \033[35m{notaar:.1f}\033[m \033[33mna prova\033[m', end='')
            print(f'\033[35m 3\033[m \033[33mpara ser aprovado por arredondamento de média\033[m')
        if notapf <= 0:
            print('\033[32mJá aprovado!!\033[m')
        if notaar > 10:
            print('\033[31mJá reprovado!!\033[m')
    if lista[3][0] == 0 and lista[0][0] > 0 and lista[1][0] > 0 and lista[2][0] > 0:
        notapf = setenta * 10 / 4.0
        notaar = arred * 10 / 4.0
        if 0 < notapf <= 10:
            print(f'\033[34mVocê terá que tirar\033[m \033[32m{notapf:.1f}\033[m \033[34mna prova\033[m', end='')
            print(f'\033[32m 4\033[m \033[34mpara ser aprovado\033[m')
        if 0 < notaar <= 10:
            print(f'\033[33mVocê terá que tirar\033[m \033[35m{notaar:.1f}\033[m \033[33mna prova\033[m', end='')
            print(f'\033[35m 4\033[m \033[33mpara ser aprovado por arredondamento de média\033[m')
        if notapf <= 0:
            print('\033[32mJá aprovado!!\033[m')
        if notaar > 10:
            print('\033[31mJá reprovado!!\033[m')
    print('\033[32m==\033[m' * 41)
if lista[3][0] != 0 and lista[0][0] != 0 and lista[1][0] != 0 and lista[2][0] != 0:
    print(f'\033[36;41m{"Considerações finais":^82}\033[m')
    print('\033[32m==\033[m' * 41)
    if soma >= 7:
        print(f'\033[34m{"Sua média final foi:":<32}\033[m', end='')
        print(f'\033[32m{soma:.3f}\033[m')
        print('\033[32mAprovadíssimo!!!!!\033[m')
    elif 6.52 <= soma < 7:
        print(f'\033[34m{"Sua média final foi:":<32}\033[m', end='')
        print(f'\033[33m{soma:.3f}\033[m')
        print(f'\033[34m{"Arredondada para:":<32}\033[m\033[32m{"7.000"}\033[m')
        print('\033[32mAprovado!!!\033[m')
    elif 6.52 > soma >= 4:
        print(f'\033[34m{"Sua média final foi:":<32}\033[m', end='')
        print(f'\033[31m{soma:.3f}\033[m')
        print('\033[31mReprovado :(\033[m')
        print('\033[34mPorém poderá refazer a matéria sem custos\033[m')
    elif 4 > soma >= 0:
        print(f'\033[34m{"Sua média final foi:":<32}\033[m', end='')
        print(f'\033[31m{soma:.3f}\033[m')
        print('\033[31mReprovado :(\033[m')
        print('\033[34mTerá custos adicionais para refazer a matéria\033[m')
    print('\033[32m==\033[m' * 41)
