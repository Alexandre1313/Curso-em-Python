def notas(*num, sit=False):
    """
    -> Função "Notas":
    param num: recebe duas ou várias notas de um determinado aluno
    param sit: valor opcional, se deve ou não incluir no dicionário a situação do aluno
    return: um dicionário com total notas, maior e menor nota, média, e se requerido a situação
    """
    dicio = {}
    maior = menor = soma = cont = total = 0
    for c in num:
        total = total + 1
        soma = soma + c
        if cont == 0:
            maior = c
            menor = c
        else:
            if c > maior:
                maior = c
            if c < menor:
                menor = c
        cont = cont + 1
    media = soma / total
    media1 = f'{soma / total:.1f}'
    dicio['Total de notas'] = total
    dicio['Maior nota'] = maior
    dicio['Menor nota'] = menor
    dicio['Média'] = media1
    if sit:
        if media < 5:
            dicio['Situação'] = 'RUIM'
        elif 5 <= media < 7:
            dicio['Situação'] = 'RAZOÁVEL'
        elif 7 <= media < 9:
            dicio['Situação'] = 'BOA'
        elif media >= 9:
            dicio['Situação'] = 'ÓTIMA'
    return dicio


alu = notas(3, 4, 2, sit=True)
print('\033[31mAbaixo cálculos conforme solicitado:\033[m')
for k, v in alu.items():
    print(f'\033[34m{k:<14}\033[m \033[34m:\033[m \033[32m{v:<8}\033[m')
print(alu)
help(notas)
