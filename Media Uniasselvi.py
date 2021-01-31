soma = 0
while True:
    try:
        prova1 = float(input('Nota da prova 1:  '))
    except (ValueError, TypeError):
        print('\033[31mInforme uma nota válida!!\033[m')
    else:
        media1 = prova1 * 1.50 / 10
        soma = soma + media1
        break
while True:
    try:
        prova2 = float(input('Nota da prova 2:  '))
    except (ValueError, TypeError):
        print('\033[31mInforme uma nota válida!!\033[m')
    else:
        media2 = prova2 * 1.50 / 10
        soma = soma + media2
        break
while True:
    try:
        prova3 = float(input('Nota da prova 3:  '))
    except (ValueError, TypeError):
        print('\033[31mInforme uma nota válida!!\033[m')
    else:
        media3 = prova3 * 3 / 10
        soma = soma + media3
        break
while True:
    try:
        prova4 = float(input('Nota da prova 4:  '))
    except (ValueError, TypeError):
        print('\033[31mInforme uma nota válida!!\033[m')
    else:
        media4 = prova4 * 4 / 10
        soma = soma + media4
        break
media5 = soma
falta = 6.52 - media5
notapf = 0
if media1 == 0 and media2 > 0 and media3 > 0 and media4 > 0:
    notapf = falta * 10 / 1.5
    print(f'\033[32mVocê terá que tirar\033[m \033[36m{notapf:.1f}\033[m \033[32mna prova\033[m', end='')
    print(f'\033[36m 1\033[m \033[32mpara ser aprovado!!\033[m')
if media2 == 0 and media1 > 0 and media3 > 0 and media4 > 0:
    notapf = falta * 10 / 1.5
    print(f'\033[32mVocê terá que tirar\033[m \033[36m{notapf:.1f}\033[m \033[32mna prova\033[m', end='')
    print(f'\033[36m 2\033[m \033[32mpara ser aprovado!!\033[m')
if media3 == 0 and media1 > 0 and media2 > 0 and media4 > 0:
    notapf = falta * 10 / 3
    print(f'\033[32mVocê terá que tirar\033[m \033[36m{notapf:.1f}\033[m \033[32mna prova\033[m', end='')
    print(f'\033[36m 3\033[m \033[32mpara ser aprovado!!\033[m')
if media4 == 0 and media1 > 0 and media2 > 0 and media3 > 0:
    notapf = falta * 10 / 4
    print(f'\033[32mVocê terá que tirar\033[m \033[36m{notapf:.1f}\033[m \033[32mna prova\033[m', end='')
    print(f'\033[36m 4\033[m \033[32mpara ser aprovado!!\033[m')
mediaf = ((prova1 * 1.5) + (prova2 * 1.5) + (prova3 * 3) + (prova4 * 4)) / 10
if 7 > mediaf >= 6.52:
    mediaf = 7
if 7 <= mediaf <= 10:
    if media1 != 0 and media2 != 0 and media3 != 0 and media4 != 0:
        print(f'''\033[32mSua média final é\033[m \033[36m{mediaf:.1f}\033[m
\033[32mParabéns, você foi aprovado :)\033[m''')
elif 7 > mediaf >= 4:
    if media1 != 0 and media2 != 0 and media3 != 0 and media4 != 0:
        print(f'''\033[32mSua média final é\033[m \033[36m{mediaf:.1f}\033[m
\033[33mInfelizmente você foi reprovado :[, mas pode refazer a matéria  sem custo\033[m''')
elif 4 > mediaf > 0:
    if media1 != 0 and media2 != 0 and media3 != 0 and media4 != 0:
        print(f'''\033[32mSua média final é\033[m \033[36m{mediaf:.1f}\033[m
\033[33mInfelizmente você foi reprovado :(, e terá custos para refazer a matéria\033[m''')
