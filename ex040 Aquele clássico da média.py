nota_1 = float(input('Informe a 1ª nota:  '))
nota_2 = float(input('Informe a 2ª nota:  '))
media = (nota_1 + nota_2) / 2
print(f'Tirando {nota_1} e {nota_2} a média do aluno é {media}')
if media < 5:
    print('O ALUNO ESTÁ REPROVADO!')
elif 5 <= media < 7:
    print('O ALUNO ESTÁ DE RECUPERAÇÃO!')
elif media >= 7:
    print('O ALUNO ESTA APROVADO!')
