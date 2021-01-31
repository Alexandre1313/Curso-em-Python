from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento:  '))
idade = atual - nasc
if nasc > atual:
    print('Opção inválida, tente novamente')
elif idade <= 9:
    print(f'O atleta tem {idade} anos.')
    print('Classificação MIRIM')
elif 9 < idade <= 14:
    print(f'O atleta tem {idade} anos.')
    print('Classificação INFANTIL')
elif 14 < idade <= 19:
    print(f'O atleta tem {idade} anos.')
    print('Classificação JÚNIOR')
elif 19 < idade <= 25:
    print(f'O atleta tem {idade} anos.')
    print('Classificação SÊNIOR')
elif 25 < idade:
    print(f'O atleta tem {idade} anos.')
    print('Classificação MASTER')
