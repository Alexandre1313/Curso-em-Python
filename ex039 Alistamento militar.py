from datetime import date
nasc = int(input('Informe o seu ano de nascimento:  '))
sex = str(input('Sexo [M/F]:  ')).strip().upper()
atual = date.today().year
idade = atual - nasc
if nasc > atual:
    print('Opção inválida, tente novamente!')
elif sex not in 'MF':
    print('Opção inválida, tente novamente')
elif sex == 'F':
    print('Pessoas do sexo feminino estão isentas de alistamento obrigatório')
elif idade == 18:
    print(f'''\033[33mNo ano de {atual} você completa {idade} anos
Você deve se alistar IMEDIATAMENTE\033[m''')
elif idade < 18:
    print(f'''\033[32mNo ano de {atual} você completa {idade} anos
Ainda faltam {18 - idade} anos para seu alistamento, que será em {nasc + 18}\033[m''')
else:
    print(f'''\033[31mNo ano de {atual} você completa {idade} anos
Já se passaram {idade - 18} anos de seu alistamento,que deveria ter sido feito no ano de {atual - idade + 18}\033[m''')
